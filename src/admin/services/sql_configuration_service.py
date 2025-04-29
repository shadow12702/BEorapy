# Description: SqlConfigurationService

import json
from typing import List
from logger import AppLogger
from admin.data.entities.sql_configuration import SqlConfiguration
from admin.factory import AdminFactory
from core.enum.app_enum import AppEnum

class SqlConfigurationService():

    _logger = AppLogger().get_logger()
    
    def __init__(self, repo_factory: AdminFactory):
        self.repository = repo_factory.sql_configuration_repository()
    
    
    async def getConfiguration(self, code: int):
        '''Get SQL Configuration by code

		:param code: is configuration code
		:return: A SqlConfiguration model'''
        return await self.repository.getById(code)
        
    
    async def getAllConfigurations(self):
        '''Get all SqlConfigurations

        :return: List of all SqlConfigurations'''
        return await self.repository.getAll()
        
            
    async def add(self, entity: SqlConfiguration):
        '''Add SqlConfiguration

        :param entity: SqlConfiguration model'''
        await self.repository.add(entity)
        
    async def addMany(self, entities: List[SqlConfiguration]):
        '''Add multiple SqlConfigurations 

        :param entities: List of SqlConfigurations'''
        try:
            data = [(e.Code, e.Value, e.Idx, e.IsUsed) for e in entities]
            await self.repository.add_many(data)
        except Exception as ex:
            self._logger.error(f"addMany SqlConfigurations error: \n{entities.__repr__()}\n{ex}")
        
    async def update(self, id: int, entity: SqlConfiguration):
        '''Update SqlConfiguration

        :param id: Id of SqlConfiguration will be updated
        :param entity: new SqlConfiguration information need to update'''
        await self.repository.update(id, entity)
        
    
    async def delete(self, id: int):
        '''Delete SqlConfiguration

        :param id: Id of the SqlConfiguration will be deleted'''
        await self.repository.delete(id)
        
    
    async def initSqlConfiguration(self):
        '''
        Initialization SqlConfiguration from json to database
        '''
        try:
            self.repository.clearAll()            
            with open(AppEnum.SQL_CONFIGURATION_FILE.value, 'r') as js_file:
                js_data = json.load(js_file)
            sql_configurations: List[SqlConfiguration] = []
            for category, items in js_data.items():
                for sub_key, attributes in items.items():
                    sql_configurations.append(SqlConfiguration.from_dict({
                        "CF_CODE": f"{category}.{sub_key}",
                        "CF_VALUE": attributes["key"],
                        "CF_IDX": attributes["index"],
                        "CF_IS_USED": attributes["is_used"]
                        })
                    )
            await self.addMany(sql_configurations)
        except Exception as ex:
            self._logger.error(f"Upload SQL Configuration failed. \nError: {ex}")
            