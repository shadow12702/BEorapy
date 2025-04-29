import asyncio
import re
from numpy import int32
from typing import Optional, Dict, List, Any, Tuple
import cx_Oracle
from logger import AppLogger
from data.db_context import DataOperators, DbContext
from core.config.config_loader import cf_loader
from threading import Lock


class OracleDbContext(DbContext, DataOperators):
    '''Oracle DbContext '''
    _pool = None
    _lock = Lock()
    _logger = AppLogger().get_logger()
    
    def __init__(self):
        '''Oracle DB Context'''
        self.db_context = cf_loader.db_context
        self.Mode = cx_Oracle.SYSDBA if self.db_context.Username == 'sys' else None
        # self.connection = None
        
    
    def _initialiize_pool(self):
        '''Initialize the connection pool if not already initialized.'''
        with self._lock:
            if OracleDbContext._pool is None:
                try:
                    if self.Mode is not None:
                        OracleDbContext._pool = cx_Oracle.SessionPool(
                            user=self.db_context.Username,
                            password=self.db_context.Password,
                            dsn=self.db_context.Dsn,
                            min=self.db_context.MinPoolSize,
                            max=self.db_context.MaxPoolSize,
                            increment=self.db_context.Increment,
                            threaded=True,
                            getmode=cx_Oracle.SPOOL_ATTRVAL_WAIT,
                            session_callback=lambda conn: conn.startup(mode=self.Mode)
                        )
                    else:
                        OracleDbContext._pool = cx_Oracle.SessionPool(
                            user=self.db_context.Username,
                            password=self.db_context.Password,
                            dsn=self.db_context.Dsn,
                            min=self.db_context.MinPoolSize,
                            max=self.db_context.MaxPoolSize,
                            increment=self.db_context.Increment,
                            threaded=True,
                            getmode=cx_Oracle.SPOOL_ATTRVAL_WAIT
                        )
                    self._logger.info("Connection pool created successfully")
                except Exception as ex:
                    self._logger.error(f"Error creating connection pool: {ex}\nConnection Info: {self.__repr__()}")
                    raise ex
    
    def connect(self):
        '''Establish a connection to database '''
        if OracleDbContext._pool is None:
            self._initialiize_pool()
        try:
            connection = OracleDbContext._pool.acquire()            
            return connection
        except Exception as ex:
            self._logger.error(f"Failed to acquire connection from pool: {ex}")
            raise ex
    
    def close(self):
        return super().close()

    def release(self, connection):
        '''Release the connection back to the pool.'''
        try:
            OracleDbContext._pool.release(connection)
        except Exception as ex:
            self._logger.error(f"Failed to release connection back to pool: {ex}")
            raise ex
    
    def begin_transaction(self, connection):
        connection.begin()

    def commit(self, connection):
        connection.commit()

    def rollback(self, connection):
        connection.rollback()
        
    async def get_data(self, query:str, params: Optional[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
        '''Execute a SELECT query and fetch the results as a list of dictionaries.
        
        Args:
            query: The SELECT query string.
            params: Optional dictionary of query parameters.
        
        Returns:
            List of dictionaries representing the rows.'''
        def sync_query():
            rows = []
            try:
                connect = self.connect()
                cursor = connect.cursor()
                cursor.execute(query, params or {})
                columns = [col[0] for col in cursor.description]
                rows.extend([{ 
                    col_name: value.read() if isinstance(value, cx_Oracle.LOB) else value 
                    for col_name, value in zip(columns, row)
                    } for row in cursor
                ])
            except Exception as ex:
                self._logger.error(f"Get data: {query}|{params}\n{ex}")
                raise ex
            finally:
                cursor.close()
                self.release(connect)
                return rows
        return await asyncio.to_thread(sync_query)
    
    async def exec_dbms_output (self, query:str, params: Optional[Dict[str, Any]] = None, buffer_size:int32=500000) -> List:
        '''Execute a PL/SQL statment and fetch the results as a list.
        
            Args:
                query: The PL/SLQ statement.
                params: Optional dictionary of query parameters.
                buffer_size: The buffer size for getting result from output.
            
            Returns:
                List output of dbms_output
        '''
        def sync_exec_plsql():
            result = []
            try:
                connect = self.connect() 
                cursor = connect.cursor()
                cursor.callproc("dbms_output.enable", [buffer_size])
                cursor.execute(query, params or {})
                v_text  = cursor.var(str)
                v_status = cursor.var(int)
                while True:
                    cursor.callproc("dbms_output.get_line", (v_text, v_status))
                    if v_status.getvalue() != 0:
                        break
                    result.append(v_text.getvalue())
            except Exception as ex:
                self._logger.error(f"Execute PL/SQL \n{ex}")
                raise ex
            finally:
                cursor.close()
                self.release(connect)
                return result
        return await asyncio.to_thread(sync_exec_plsql)
        
    async def execute_query(self, query:str, params:Optional[Dict[str, Any]]=None):
        '''Execute none query
        
        Args:
            query (str): None query statement
            params (dict): Optional dictionary of none query parameter        
        '''
        def sync_exec_query():
            v_result = 0
            try:
                connect = self.connect()
                self.begin_transaction(connect)
                cursor = connect.cursor()
                cursor.execute(query, params or {})
                self.commit(connect)
            except Exception as ex:
                self._logger.error(f"execute query: {query}|{params}\n{ex}")
                self.rollback(connect)
                raise ex
            finally:
                cursor.close()
                self.release(connect)
                return v_result
        return await asyncio.to_thread(sync_exec_query)
    
    async def execute_many(self, query:str, params:List[Tuple[Any]]):
        '''Execute none query with bulk data 
        
        Args:
            query (str): None query statement
            params (list[tuple()]): List of tuple, where each tuple contains the object details in none query parameter        
        '''
        def sync_exec_many():
            v_result = 0
            try:
                connect = self.connect()
                self.begin_transaction(connect)
                cursor = connect.cursor()
                cursor.executemany(query, params)
                self.commit(connect)
                return cursor.rowcount
            except Exception as ex:
                self.rollback(connect)
                self._logger.error(f"executeMany error: \n{query}|({params})\n{ex}")
                raise ex
            finally:
                cursor.close()
                self.release(connect)
                return v_result
        return await asyncio.to_thread(sync_exec_many)
    

    async def call_plsql(self, plsql:str, input_params: Optional[Dict[str, Any]] = None):
        '''Call a block PL/SQL with dynamic input parameters and output cursor.
        
        Args:
            plsql (str): block PL/SQL.
            input_params: Dictionary of input parameters.
                        
        Returns:
            List data as the result of block PL/SQL.
        '''
        def preprocess_plsql(plsql):
            # Remove single-line comments (starting with --)
            plsql_no_comments = re.sub(r"--.*", "", plsql)
            # Replace literals in quotes (e.g., 'text' or 'mm/dd/yyyy HH24:MI') with placeholders
            return re.sub(r"'[^']*'", "''", plsql_no_comments)
        
        def sync_call():
            results = []
            try:
                preprocessed_plsql = preprocess_plsql(plsql)
                # Use regex to find valid bind variables
                output_vars = re.findall(r":([a-zA-Z_][a-zA-Z0-9_]*)", preprocessed_plsql)
                
                connect = self.connect()
                cursor = connect.cursor()
                params = input_params or {}
                output_vars = [var for var in output_vars if var not in input_params.keys()]
                
                for var in output_vars:
                    params[var] = cursor.var(cx_Oracle.CURSOR)
                cursor.execute(plsql, params)

                for var in output_vars:
                    if hasattr(params[var], "getvalue"):  # Ensure the variable has a `getvalue()` method
                        output_cursor = params[var].getvalue()                    
                        columns = [col[0] for col in output_cursor.description]
                        output_data = []
                        for row in output_cursor.fetchall():
                            row_dict = {col: (value.read() if isinstance(value, cx_Oracle.LOB) else value) for col, value in zip(columns, row)}
                            output_data.append(row_dict)
                        results.append(output_data)
                    # return results[0] if len(results) == 1 else results
            except Exception as ex:
                self._logger.error(f"execute block PL/SQL:\n{plsql}\nParams: {input_params}\n{ex}")
                raise ex
            finally:
                cursor.close()
                self.release(connect)
                return results
        return await asyncio.to_thread(sync_call)
    
    async def call_procedure(self, proc_name: str, input_params: Optional[Dict[str, Any]] = None, output_cursor: bool = False):
        """Call a stored procedure with dynamic input parameters and optional output cursor.
        
        Args:
            proc_name: Name of the stored procedure.
            input_params: Dictionary of input parameters.
            output_cursor: If True, expect an output cursor.
        
        Return: 
            If output_cursor is True, returns the fetched data; otherwise, returns None.
        """
        def sync_procedure():
            try:
                params = []
                if input_params:
                    params.extend(input_params.values())
                connect = self.connect()
                cursor = connect.cursor()
                #handle output cursor when having in procedure
                if output_cursor:
                    out_cursor = cursor.var(cx_Oracle.CURSOR)
                    params.append(out_cursor)
                    _ = cursor.callproc(proc_name, params)
                    output_data = out_cursor.getvalue().fetchall()

                    # format the output data as a list of dictionaries
                    columns = [col[0] for col in out_cursor.getvalue().description]
                    res_formated = [dict(zip(columns, row)) for row in output_data]
                    return res_formated
                else:
                    cursor.callproc(proc_name, params)
            except Exception as ex:
                self._logger.error(f"call Procedure:{proc_name}({input_params},{output_cursor})\n{ex}")
                raise ex
            finally:
                cursor.close()
                self.release(connect)
        return await asyncio.to_thread(sync_procedure)
    

    async def call_function(self, func_name: str, input_params: Optional[Dict[str, Any]] = None, return_type: Any = cx_Oracle.STRING) -> Any:
        """Call a stored function with dynamic input parameters and a specified return type.
        
        Args:
            func_name: Name of the stored function.
            input_params: Dictionary of input parameters.
            return_type: Expected return type of the Oracle function.
        
        Return: 
            The function's return value, or fetched data if it returns a cursor.
        """        
        def sync_function():
            try:
                # Prepare parameters for input
                params = []
                if input_params:
                    params.extend(input_params.values())
                
                connect = self.connect()
                cursor = connect.cursor()
                result = cursor.callfunc(func_name, return_type, params)
                # If return_type is CURSOR,  then process to return a list of dict
                if return_type == cx_Oracle.CURSOR:
                    output_data = result.fetchall()  
                    columns = [col[0] for col in result.description]  
                    res_formated = [dict(zip(columns, row)) for row in output_data]
                    return res_formated
                # return value of function with type from return_type
                return result
            except Exception as ex:
                self._logger.error(f"call Function: {func_name}({input_params})\n{ex}")
                raise ex
            finally:
                cursor.close()
                self.release(connect)
        return await asyncio.to_thread(sync_function)
    