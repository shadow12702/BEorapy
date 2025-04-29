from data.db_context import DbContext, DataOperators
from app.data.entities.db_version import DbVersion
from app.data.entities.db_open_mode import DbOpenMode
from app.data.entities.checkdb import CheckDb 
from app.data.repositories.enum.common_enum import CommonEnum
from logger import AppLogger
from typing import List

class CommonRepository():
    _logger = AppLogger().get_logger()
    
    def __init__(self, db_context: DbContext):        
        if not isinstance(db_context, DataOperators):
            self._logger.error(TypeError("db_context must implement DataOperations"))
        
        self.db_context = db_context
        
    
    def checkDbStatus(self, db_name:str):
        try:
            query = self.redis.getKey(CommonEnum.CHECK_DB_STATUS.value)
            data = self.db_context.callPlSql(plsql=query, 
                                           input_params={'P_DB_NAME': db_name})
            checkdb = [CheckDb(**d) for d in data] if data else List[CheckDb.empty()]
            return checkdb
        except Exception as ex:
            self._logger.error(f"CheckDbStatus error: {ex}")
            
    def getDbName(self, dbid):
        try:
            query = self.redis.getKey(CommonEnum.GET_DATABASE_NAME.value)
            dbName = self.db_context.getData(query=query, params={'P_DBID': dbid})
            return dbName
        except Exception as ex:
            self._logger.error(f"GetDbName error: {ex}")
            return ''
        
    def getDbVersion(self) -> DbVersion:
        try:
            query = self.redis.getKey(CommonEnum.GET_DB_VERSION.value)            
            data = self.db_context.getData(query)
            version = DbVersion(**data[0]) if data else DbVersion.empty()
            return version
        except Exception as ex:
            self._logger.error(f"Get DbVersion error: {ex}")
            return DbVersion.empty()

    def getDbOpenMode(self) -> DbOpenMode:
        try:            
            query = self.redis.getKey(CommonEnum.GET_DB_OPEN_MODE.value)            
            data = self.db_context.getData(query)
            mode = DbOpenMode(**data[0]) if data else DbOpenMode.empty()
            return mode
        except Exception as ex:
            self._logger.error(f"Get DbOpenMode error: {ex}")
            return DbOpenMode.empty()
