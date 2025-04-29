from data.db_context import DbContext, DataOperators
from logger import AppLogger
from base.domain.base_repository import BaseRepository
from admin.data.entities.language import Language
from typing import List

class LanguageRepository(BaseRepository):
    _logger = AppLogger().get_logger()
    
    def __init__(self, db_context: DbContext, language: str='en'):        
        if not isinstance(db_context, DataOperators):
            self._logger.error(TypeError("db_context must be a part of DataOperators"))
        self.language = language
        self.db_context = db_context
        
    async def get_by_id(self, code:str) -> Language:
        '''Get language by code
        
        :param code: is language code
        :return: A Language model'''        
        try:
            query = "SELECT * FROM SYS_LANGUAGE WHERE CODE = :V_CODE"
            lang = await self.db_context.get_data(query, {'V_CODE': code})
            return Language(**lang) if lang else Language.empty()            
        except Exception as ex:
            self._logger.error(f"Get language ById error {ex}")


    async def get_all(self) -> List[Language]:
        '''Get all languages
        
        :return: List of all languages'''
        try:
            query = "SELECT * FROM SYS_LANGUAGE ORDER BY DISPLAY_ORDER"
            data= await self.db_context.get_data(query)
            return [Language(**lang) for lang in data] if data else List[Language.empty()]            
        except Exception as ex:
            self._logger.error(f"Get language error {ex}")
    

    async def add(self, entity: Language):
        '''Add language
        
        :param entity: Language model'''
        try:
            query = """INSERT INTO SYS_LANGUAGE(CODE, LANG_NAME, LANG_CULTURE, LANG_FLAG_NAME, IS_PUBLISHED, DISPLAY_ORDER)
                       VALUES (:V_CODE, :V_NAME, :V_CULTURE, :V_FLAG_NAME, :V_IS_PUBLISHED, :V_ORDER)
                       """
            await self.db_context.execute_query(query, {'V_CODE':entity.Code,
                                                 'V_NAME':entity.Name,
                                                 "V_CULTURE": entity.Culture,
                                                 "V_FLAG_NAME":entity.FlagName,
                                                 "V_IS_PUBLISHED":entity.IsPublished,
                                                 "V_ORDER":entity.DisplayOrder
                                                 })
        except Exception as ex:
            self._logger.error(f"Add language error: \n{entity.__repr__()} \n{ex}")

    async def update(self, id: str, entity: Language):
        '''Update language
        
        :param id: Id of language will be updated
        :param entity: new Language information need to update'''
        try:
            query = """UPDATE SYS_LANGUAGE 
                       SET CODE            = :V_CODE,
                           LANG_NAME       = :V_NAME,
                           LANG_CULTURE    = :V_CULTURE,
                           LANG_FLAG_NAME  = :V_FLAG_NAME,
                           IS_PUBLISHED    = :V_IS_PUBLISHED,
                           DISPLAY_ORDER   = :V_ORDER
                      WHERE ID = :V_ID"""
            await self.db_context.execute_query(query, {'V_ID': id, 
                                                 'V_CODE':entity.Code,
                                                 'V_NAME':entity.Name,
                                                 "V_CULTURE": entity.Culture,
                                                 "V_FLAG_NAME":entity.FlagName,
                                                 "V_IS_PUBLISHED":entity.IsPublished,
                                                 "V_ORDER":entity.DisplayOrder
                                                 })
        except Exception as ex:
            self._logger.error(f"Update language error: \n id:{id} \n{entity.__repr__()} \n{ex}")

    async def delete(self, id):
        '''Delete language
        
        :param id: Id of the language will be deleted'''
        try:
            query = "DELETE FROM SYS_LANGUAGE WHERE ID = :V_ID"
            return await self.db_context.execute_query(query, {'V_ID': id})
        except Exception as ex:
            self._logger.error(f"Delete language error: \nid: {id} \n{ex}")
    