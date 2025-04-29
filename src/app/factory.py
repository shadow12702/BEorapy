from functools import lru_cache
from data.db_context import DbContext
from logger import AppLogger
from app.data.repository import *

class ApplicationFactory:
    '''
    CommonRepositoyFactory class to manage repository intances
    '''    
    _logger = AppLogger().get_logger()

    def __init__(self, db_context: DbContext):
        self.db_context = db_context
    
    @lru_cache(maxsize=1)
    def common_repository(self) -> CommonRepository:
        '''Get Common Repository
        '''
        try:
            return CommonRepository(self.db_context)
        except Exception as ex:
            self._logger.error(f'CommonRepository initialize failure.\n{ex}')
        
    @lru_cache(maxsize=1)        
    def awr_repo_info_repository(self) -> AwrRepoInfoRepository:
        '''Get Awr Repo Info Repository
        '''
        try:
            return AwrRepoInfoRepository(self.db_context)
        except Exception as ex:
            self._logger.error(f'AwrRepository initialize failure.\n{ex}')
    
    @lru_cache(maxsize=1)
    def addm_repository(self) -> AddmRepository:
        '''Get Addm Repository
        '''
        try:
            return AddmRepository(self.db_context)
        except Exception as ex:
            self._logger.error(f'AddmRepository initialize failure.\n{ex}')
    
    @lru_cache(maxsize=1)
    def cdb_ash_overall_repository(self) -> CdbAshOverallRepository:
        '''Get Cdb Repository
        '''        
        try:
            return CdbAshOverallRepository(self.db_context)
        except Exception as ex:
            self._logger.error(f'CdbRepository initialize failure.\n{ex}')
    
    @lru_cache(maxsize=1)
    def non_cdb_repository(self) -> NonCdbRepository:
        '''Get NonCdb Repository
        '''
        try:
            return NonCdbRepository(self.db_context)
        except Exception as ex:
            self._logger.error(f'NonCdbRepository initialize failure.\n{ex}')