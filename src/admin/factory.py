# Description: All factories of Admin will define here

from functools import lru_cache
from data.oracle_db_context import DbContext
from admin.data.repository import *
from logger import AppLogger

class AdminFactory:
    '''
    Factory class to manage repository intances
    '''
    _logger = AppLogger().get_logger()

    def __init__(self, db_context: DbContext):
        self.db_context = db_context
    
    @lru_cache(maxsize=1)
    def language_repository(self, language:str = 'en') -> LanguageRepository:
        '''Get language repository
        '''
        try:
            return LanguageRepository(self.db_context, language)
        except Exception as ex:
            self._logger.error(f"languageReporisoty: \n{ex}")
    
    @lru_cache(maxsize=1)
    def sql_configuration_repository(self) -> SqlConfigurationRepository:
        '''Get SqlConfiguration repository
        '''
        try:
            return SqlConfigurationRepository(self.db_context)
        except Exception as ex:          
            self._logger.error(f"sqlConfigurationRepository: \n{ex}")
    
    @lru_cache(maxsize=1)        
    def config_repository(self):
        return ConfigRepository(self.db_context)
        
    @lru_cache(maxsize=1)        
    def account_repository(self) -> AccountRepository:
        '''Get account repository
        '''
        try:
            return AccountRepository(self.db_context)
        except Exception as ex:          
            self._logger.error(f"accountRepository: \n{ex}")
            
    @lru_cache(maxsize=1)        
    def config_repository(self) -> ConfigRepository:
        '''Get Config repository
        '''
        return ConfigRepository(self.db_context)
    
    @lru_cache(maxsize=1)        
    def menu_repository(self) -> MenuRepository:
        '''Get Menu repository
        '''
        return MenuRepository(self.db_context)
    
    @lru_cache(maxsize=1)
    def customers_repository(self) -> CustomerRepository:
        '''Get Customers repository
        '''
        return CustomerRepository(self.db_context)
    
    @lru_cache(maxsize=1)
    def patch_repository(self) -> PatchRepository:
        '''Get patch repository
        '''
        return PatchRepository(self.db_context)
    
    @lru_cache(maxsize=1)
    def best_practice_repository(self) -> BestPracticeRepository:
        '''Get Practice repository
        '''
        return BestPracticeRepository(self.db_context)