from logger import AppLogger
from data.db_context import DbContext, DataOperators
from admin.data.entities.best_practice import BestPractice
from helper import helper
from typing import List

class BestPracticeRepository():
    _logger = AppLogger().get_logger()
    
    def __init__(self, db_context: DbContext):
        if not isinstance(db_context, DataOperators):
            self._logger.error(TypeError("db_context must be a part of DataOperators"))
        self.db_context = db_context
        
    
    async def get_all(self) -> List[BestPractice]:
        '''Get all best practices'''
        try:
            query = """SELECT ID, BP_DB_VERSION, BP_PARAMETER, BP_PARAM_DEFAULT_VALUE, BP_PARAM_RECOMMEND_VALUE, BP_FOR_RAC_ONLY, BP_NOTES FROM SYS_BEST_PRACTICE"""
            practices = await self.db_context.get_data(query)
            return [BestPractice(**p) for p in practices]
        except Exception as ex:
            self._logger.error(f"Get all best practices error {ex}")
            
    
    async def get_by_id(self, id:int) -> BestPractice:
        '''Get best practice by ID'''
        try:
            query = """SELECT ID, BP_DB_VERSION, BP_PARAMETER, BP_PARAM_DEFAULT_VALUE, BP_PARAM_RECOMMEND_VALUE, BP_FOR_RAC_ONLY, BP_NOTES FROM SYS_BEST_PRACTICE WHERE ID = :V_ID"""
            practice = await self.db_context.get_data(query, {"V_ID": id})
            return [BestPractice(**p) for p in practice]
        except Exception as ex:
            self._logger.error(f"Get best practice error {ex}")
            
    
    async def add(self, entity: BestPractice):
        '''Add new best practice'''
        try:
            query = """ INSERT INTO SYS_BEST_PRACTICE (BP_DB_VERSION, BP_PARAMETER, BP_PARAM_DEFAULT_VALUE, BP_PARAM_RECOMMEND_VALUE, BP_FOR_RAC_ONLY, BP_NOTES, CREATED_UTC, UPDATED_UTC)
                        VALUES(:V_DB_VERSION, :V_PARAMETER, :V_DEFAULT_VALUE, :V_RECOMMEND_VALUE, :V_FOR_RAC_ONLY, :V_NOTES, SYSDATE, SYSDATE)"""
            return await self.db_context.execute_query(query, {
                "V_DB_VERSION": entity.DbVersion,
                "V_PARAMETER": entity.Parameter,
                "V_DEFAULT_VALUE": entity.ParamDefaultValue,
                "V_RECOMMEND_VALUE": entity.ParamRecommendValue,
                "V_FOR_RAC_ONLY": entity.ForRacOnly,
                "V_NOTES": entity.Notes,
            })
        except Exception as ex:
            self._logger.error(f"Add error {ex}")
    
    async def update(self, id:int, entity: BestPractice):
        '''Update best practice'''
        try:
            query = """UPDATE SYS_BEST_PRACTICE
                SET BP_DB_VERSION = :V_BP_DB_VERSION,
                    BP_PARAMETER = :V_PARAMETER,
                    BP_PARAM_DEFAULT_VALUE = :V_DEFAULT_VALUE,
                    BP_PARAM_RECOMMEND_VALUE = :V_RECOMMEND_VALUE,
                    BP_FOR_RAC_ONLY = :V_FOR_RAC_ONLY,
                    BP_NOTES = :V_NOTES,
                    UPDATED_UTC = SYSDATE
                WHERE ID = :V_ID"""
            return await self.db_context.execute_query(query, {
                "V_ID": id,
                "V_BP_DB_VERSION": entity.DbVersion,
                "V_PARAMETER": entity.Parameter,
                "V_DEFAULT_VALUE": entity.ParamDefaultValue,
                "V_RECOMMEND_VALUE": entity.ParamRecommendValue,
                "V_FOR_RAC_ONLY": entity.ForRacOnly,
                "V_NOTES": entity.Notes,
            })
        except Exception as ex:
            self._logger.error(f"Update error {ex}")

    async def delete(self, id:int):
        '''Delete best practice'''
        try:
            query = "DELETE FROM SYS_BEST_PRACTICE WHERE ID = :V_ID"
            return await self.db_context.execute_query(query, {"V_ID": id})
        except Exception as ex:
            self._logger.error(f"Delete error {ex}")
    
    async def clear_all(self):
        '''Delete all best practices'''
        try:
            query = "TRUNCATE TABLE SYS_BEST_PRACTICE"
            return await self.db_context.execute_query(query)
        except Exception as ex:
            self._logger.error(f"Clear all failed. Error: {ex}")