from data.db_context import DbContext, DataOperators
from logger import AppLogger
from base.domain.base_repository import BaseRepository
from admin.data.entities.sql_configuration import SqlConfiguration
from typing import List, Tuple

class SqlConfigurationRepository(BaseRepository):
    _logger = AppLogger().get_logger()

    def __init__(self, db_context: DbContext):
        if not isinstance(db_context, DataOperators):
            self._logger.error(TypeError("db_context must be a part of DataOperators"))
        self.db_context = db_context


    async def get_by_id(self, code:str) -> SqlConfiguration:
        '''Get SQL Configuration by code

        :param code: configuration code
        :return: A SqlConfiguration model'''
        try:            
            query = "SELECT * FROM SYS_SQL_CONFIGURATION WHERE CF_CODE = :V_CODE AND CF_IS_USED = :V_IS_USED"
            data = await self.db_context.get_data(query, {'V_CODE': code, 'V_IS_USED': 1})
            return SqlConfiguration(**data) if data else SqlConfiguration.empty()
        except Exception as ex:
            self._logger.error(f"getById error {ex}")


    async def get_all(self) -> List[SqlConfiguration]:
        '''Get all SqlConfigurations

        :return: List of all SqlConfigurations'''
        try:
            query = "SELECT * FROM SYS_SQL_CONFIGURATION ORDER BY CF_IDX"
            data= await self.db_context.get_data(query)
            return [SqlConfiguration(**cf) for cf in data] if data else List[SqlConfiguration.empty()]
        except Exception as ex:
            self._logger.error(f"getAll error {ex}")

    async def get_active_sql_configurations(self) -> List[SqlConfiguration]:
        '''Get all activte SqlConfigurations

        :return: List of active SqlConfigurations'''
        try:
            query = """SELECT * FROM SYS_SQL_CONFIGURATION 
                WHERE CF_IS_USED = 1
                ORDER BY CF_IDX"""
            data= await self.db_context.get_data(query)
            return [SqlConfiguration(**cf) for cf in data] if data else List[SqlConfiguration.empty()]
        except Exception as ex:
            self._logger.error(f"getActiveSqlConfigurations error {ex}")


    async def add(self, entity: SqlConfiguration):
        '''Add SqlConfiguration

        :param entity: SqlConfiguration model'''
        try:
            query = """INSERT INTO SYS_SQL_CONFIGURATION(CF_CODE, CF_VALUE, CF_IDX, CF_IS_USED)
                       VALUES (:V_CODE, :V_VALUE, :V_IDX, :V_IS_USED)
                       """
            await self.db_context.execute_query(query, {'V_CODE':entity.Code,
                                                 'V_VALUE':entity.Value,
                                                 "V_IDX": entity.Idx,
                                                 "V_IS_USED":entity.IsUsed
                                                 })
        except Exception as ex:
            self._logger.error(f"Add SqlConfiguration error: \n{entity.__repr__()} \n{ex}")
    
    async def add_many(self, entities: List[Tuple[SqlConfiguration]]):
        '''Add multiple SqlConfigurations 

        :param entities: List of Tuple SqlConfigurations'''
        try:
            query = """INSERT INTO SYS_SQL_CONFIGURATION(CF_CODE, CF_VALUE, CF_IDX, CF_IS_USED)
                       VALUES (:V_CODE, :V_VALUE, :V_IDX, :V_IS_USED)
                       """            
            await self.db_context.execute_many(query, entities)
        except Exception as ex:
            self._logger.error(f"Add many SqlConfigurations error: \n{entities.__repr__()} \n{ex}")


    async def update(self, id: int, entity: SqlConfiguration):
        '''Update SqlConfiguration

        :param id: Id of SqlConfiguration will be updated
        :param entity: new SqlConfiguration information need to update'''
        try:
            query = """UPDATE SYS_SQL_CONFIGURATION
                       SET CF_CODE     = :V_CODE,
                           CF_VALUE    = :V_VALUE,
                           CF_IDX      = :V_IDX,
                           CF_IS_USED  = :V_IS_USED
                      WHERE ID = :V_ID"""
            await self.db_context.execute_query(query, {'V_ID': id,
                                                 'V_CODE':entity.Code,
                                                 'V_VALUE':entity.Value,
                                                 "V_IDX": entity.Idx,
                                                 "V_IS_USED":entity.IsUsed
                                                 })
        except Exception as ex:
            self._logger.error(f"Update SqlConfiguration error: \n id:{id} \n{entity.__repr__()} \n{ex}")

    async def delete(self, id):
        '''Delete SqlConfiguration

        :param id: Id of the SqlConfiguration will be deleted'''
        try:
            query = "DELETE FROM SYS_SQL_CONFIGURATION WHERE ID = :V_ID"
            return await self.db_context.execute_query(query, {'V_ID': id})
        except Exception as ex:
            self._logger.error(f"Delete SqlConfiguration error: \nid: {id} \n{ex}")

    async def clear_all(self):
        '''Delete all SQL Configuration
        '''
        try:
            query = "TRUNCATE TABLE SYS_SQL_CONFIGURATION"
            await self.db_context.execute_query(query)
        except Exception as ex:
            self._logger.error(f"Truncate table SYS_SQL_CONFIGURATION failed. \nError: {ex}")