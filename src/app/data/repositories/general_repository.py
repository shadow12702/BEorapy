from numpy import int32, int64
from data.db_context import DataOperators, DbContext
from app.data.entities.odb.db_info import OdbDbInfo
from app.data.entities.odb.extract_top_sql import OdbExtractTopSql
from logger import AppLogger

class GeneralRepository:    

    _logger = AppLogger().get_logger()
    
    def __init__(self, db_context: DbContext):        
        if not isinstance(db_context, DataOperators):
            self._logger.error(TypeError("db_context must implement DataOperations"))        
        self.db_context = db_context        
    
    async def get_data(self, query, model, cus_code: str, dbid:int64, begin_snap: int32, end_snap: int32):
        '''Generalized method to retrieve data based on Enum Key and model object.
        
            Args:
                enum_key: Enum Key to identify the query key
                model: The object model to instantiate the entities
                dbid: Database ID
                begin_snap: Begin snapshot
                end_snap: End snapshot
            
            Return: 
                List of model instances or an empty list
        '''
        try:             
            # query = self.redis.getKey(enum_key.value)
            data = await self.db_context.get_data(
                query=query,
                params={ 'P_CUS_CODE': cus_code,
                    'P_DBID': dbid,
                    "P_BEGIN_SNAP":begin_snap, 
                    "P_END_SNAP":end_snap
                    }
                )
            entities = [model(**e) for e in data]
            return entities
        except Exception as ex:
            self._logger.error(f"Get Value for key {query} error: {ex}")
            raise ex

    def getValue(self, query, model, dbid:int64, begin_snap: int32, end_snap: int32):
        '''Generalized method to retrieve data based on Enum Key and model object.
        
            Args:
                enum_key: Enum Key to identify the query key
                model: The object model to instantiate the entities
                dbid: Database ID
                begin_snap: Begin snapshot
                end_snap: End snapshot
            
            Return: 
                List of model instances or an empty list
        '''
        try:             
            # query = self.redis.getKey(enum_key.value)
            data = self.db_context.get_data(
                query=query,
                params={ 'P_CUS_CODE': cus_code,
                    'P_DBID': dbid,
                    "P_BEGIN_SNAP":begin_snap, 
                    "P_END_SNAP":end_snap
                    }
                )
            entities = [model(**e) for e in data] if data is not None and len(data) > 0 else [model.empty()]
            return entities
        except Exception as ex:
            self._logger.error(f"Get Value for key {query} error: {ex}")


    def getDbInfo(self, db_info_key: str, dbid:int64):
        '''Get Database Information
        
        Args:
            db_info_key: identification key to get database info
            dbid (int64): Database ID
        
        Returns:
            Database Information
        '''
        try:
            query = self.redis.getKey(db_info_key)
            data = self.db_context.execDbmsOutput(query= query,
                                           params= {
                                               'P_DBID': dbid
                                               }
                                           )
            dbinfo = []
            for item in data:
                key, value = item.split(":")
                dbinfo.append({"STAT_NAME": str(key).strip(), "STAT_VALUE": str(value).strip()})
            entities = [OdbDbInfo(**e) for e in dbinfo] if dbinfo else [OdbDbInfo.empty()]
            return entities
        except Exception as ex:
            self._logger.error(f"getDbInfo error: {ex}")
            
    
    def extractTopSql(self, enum_key, top_n_rows:int = 10):
        '''Extract Top N SQL 
        
        Args:
            enum_key: Enum Key to identify the query key
            top_n_rows: Number of records will be taken, value default is 10
            
        Return: 
            List of ExtractTopSQL instances or an empty list
        '''
        try:
            query = self.redis.getKey(enum_key.value)
            data = self.db_context.getData(
                query=query,
                params={'TOP_N_ROWS': top_n_rows}
                )
            entities = [OdbExtractTopSql(**e) for e in data] if data else [OdbExtractTopSql.empty()]
            return entities
        except Exception as ex:
            self._logger.error(f"extractTopSql for {enum_key} error: \n{ex}")
    
    