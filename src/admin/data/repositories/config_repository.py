from logger import AppLogger
from helper import helper
from data.db_context import DbContext, DataOperators
from admin.data.entities.config import Config
from typing import List

class ConfigRepository():
    _logger = AppLogger().get_logger()
    
    def __init__(self, db_context: DbContext):
        if not isinstance(db_context, DataOperators):
            self._logger.error(TypeError("db_context must be a part of DataOperators"))
        self.db_context = db_context

    async def get_config_by_type(self, type:str) -> List[Config]:
        '''Get list config info by type

        :param code: type of config
        :return: list config by type'''
        try:            
            query = """SELECT * FROM SYS_CONFIG WHERE CF_TYPE = :V_TYPE ORDER BY ID"""
            data = await self.db_context.get_data(query, {'V_TYPE': type})
            return [Config(**e) for e in data] if len(data) > 0 else []
        except Exception as ex:
            self._logger.error(f"getConfigByType error {ex}")
    
    async def get_all(self) -> List[Config]:    
        '''Get all configurations

        :return: List of all configurations'''
        try:
            query = "SELECT * FROM SYS_CONFIG WHERE CF_IS_LOCKED = 0 ORDER BY ID"
            data = await self.db_context.get_data(query)
            # return result
            return [Config(**e) for e in data] if data else []
        except Exception as ex:
            self._logger.error(f"getAll error {ex}")

    async def write(self, type:str, key:str, value: str, is_locked: int = 0):
        '''Write config to system'''
        try:
            query = """INSERT INTO SYS_CONFIG(CF_TYPE, CF_KEY, CF_VALUE, CF_IS_LOCKED, CREATED_ON_UTC, LAST_CHANGED)
            VALUES(:V_TYPE, :V_KEY, :V_VALUE, :V_IS_LOCKED, 
                TO_DATE(:V_CREATED_ON, 'DD/MM/YYYY HH24:MI:SS'), 
                TO_DATE(:V_LAST_CHANGED, 'DD/MM/YYYY HH24:MI:SS')
                )"""
            date = helper.get_date_utc()
            await self.db_context.execute_query(query, {
                "V_TYPE": type,
                "V_KEY": key,
                "V_VALUE": value,
                "V_IS_LOCKED": is_locked,
                "V_CREATED_ON": date,
                "V_LAST_CHANGED": date
            })
        except Exception as ex:
            self._logger.error(f"Write config fail {ex}")
    
    async def update(self, type: str, key: str, value: str, is_locked: int = 0):
        'Update configuration'
        try:
            date = helper.get_date_utc()  # tự sinh ra LAST_CHANGED, không cần lấy từ request
            query = """UPDATE SYS_CONFIG
                    SET CF_VALUE = :V_VALUE,
                        CF_IS_LOCKED = :V_IS_LOCKED,
                        LAST_CHANGED = TO_DATE(:V_LAST_CHANGED, 'DD/MM/YYYY HH24:MI:SS')
                    WHERE CF_TYPE = :V_TYPE
                        AND CF_KEY = :V_KEY"""
            await self.db_context.execute_query(query, {
                "V_TYPE": type,
                "V_KEY": key,
                "V_VALUE": value,
                "V_IS_LOCKED": is_locked,
                "V_LAST_CHANGED": date
            })
        except Exception as ex:
            self._logger.error(f"Update config ({type},{key}) failed {ex}")
