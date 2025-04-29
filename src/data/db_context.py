import cx_Oracle
from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional, Tuple

class DbContext(ABC):
    @abstractmethod
    def connect(self):
        '''Establish a connection to database'''
        pass
    @abstractmethod
    def close(self):
        '''Close connection'''
        pass

class DataTransactions(ABC):
    @abstractmethod
    def begin_transaction(self, connection):
        pass
    @abstractmethod
    def commit(self, connection):
        pass
    @abstractmethod
    def rollback(self, connection):
        pass

class DataOperators(ABC):
    @abstractmethod
    async def get_data(self, query:str, params: Optional[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
        '''Execute a SELECT query and fetch the results as a list of dictionaries.
        
        Args:
            query: The SELECT query string.
            params: Optional dictionary of query parameters.
        
        Returns:
            List of dictionaries representing the rows.'''
        pass
    @abstractmethod
    async def exec_dbms_output(self, query:str, params: Optional[Dict[str, Any]] = None, buffer_size:int=500000) -> List:
        '''Execute a PL/SQL statment and fetch the results as a list.
        
            Args:
                query: The PL/SLQ statement.
                params: Optional dictionary of query parameters.
                buffer_size: The buffer size for getting result from output.
            
            Returns:
                List output of dbms_output
        '''
        pass
    @abstractmethod
    async def execute_query(self, query:str, params:Optional[Dict[str, Any]]=None):
        '''Execute none query
        
        Args:
            query (str): None query statement
            params (dict): Optional dictionary of none query parameter        
        '''
        pass
    @abstractmethod
    async def execute_many(self, query:str, params:Optional[Tuple[Any]]=None):
        '''Execute none query with bulk data 
        
        Args:
            query (str): None query statement
            params (list[tuple()]): List of tuple, where each tuple contains the object details in none query parameter        
        '''
        pass
    @abstractmethod
    async def call_plsql(self, plsql:str, input_params: Optional[Dict[str, Any]] = None):
        '''Call a block PL/SQL with dynamic input parameters and output cursor.
        
        Args:
            plsql (str): block PL/SQL.
            input_params: Dictionary of input parameters.
                        
        Returns:
            List data as the result of block PL/SQL.
        '''
        pass
    @abstractmethod
    async def call_procedure(self, proc_name: str, input_params: Optional[Dict[str, Any]] = None, output_cursor: bool = False) -> Any:
        """Call a stored procedure with dynamic input parameters and optional output cursor.
        
        Args:
            proc_name: Name of the stored procedure.
            input_params: Dictionary of input parameters.
            output_cursor: If True, expect an output cursor.
        
        Return: 
            If output_cursor is True, returns the fetched data; otherwise, returns None.
        """
        pass
    @abstractmethod
    async def call_function(self, func_name: str, input_params: Optional[Dict[str, Any]] = None, return_type: Any = cx_Oracle.STRING) -> Any:
        """Call a stored function with dynamic input parameters and a specified return type.
        
        Args:
            func_name: Name of the stored function.
            input_params: Dictionary of input parameters.
            return_type: Expected return type of the Oracle function.
        
        Return: 
            The function's return value, or fetched data if it returns a cursor.
        """
        pass

