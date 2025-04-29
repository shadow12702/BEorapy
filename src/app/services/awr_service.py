# Description: 

from numpy import int32, int64
from typing import List
from app.factory import ApplicationFactory
from app.data.entities.awr import Awr
from app.data.entities.awr_html import AwrHtml
from app.data.entities.awr_config import AwrConfig
from app.data.entities.awr_healthcheck import AwrHealthcheck
from logger import AppLogger


class AwrService():
    
    _logger = AppLogger().get_logger()
    
    def __init__(self, repo_factory: ApplicationFactory):        
        self.awrRepository = repo_factory.awrRepository()

    @property
    def Awrs(self) -> List[Awr]:
        ''':return: list of Awr'''
        db_version = self.awrRepository.getAwrs()
        return float(db_version[0:4])

    @property
    def AwrsForHealthcheck(self)-> List[AwrHealthcheck]:
        ''':return: list of AwrHealthcheck'''
        data = self.awrRepository.getAwrsForHealthCheck()
        return data

    def getAwrConfig(self, dbid: int64, begin_snap: int32, end_snap:int32)-> AwrConfig:
        '''
        Get Awr configuration

        :param dbid: DBID number in Awr list
        :param begin_snap: begin snapshot number
        :param end_snap: end snapshot number
        :return: AwrConfig 
        '''        
        try:
            return self.awrRepository.getAwrConfig(dbid, begin_snap, end_snap)
        except Exception as ex:
            self._logger.error (f"get AwrConfig error: {ex}")


    def getAwrHtml(self, dbid: int64, begin_snap: int32, end_snap:int32)-> AwrHtml:
        '''
        Get Awr for generate the html

        :param dbid: DBID number in Awr list
        :param begin_snap: begin snapshot number
        :param end_snap: end snapshot number
        :return: AwrHtml 
        '''        
        try:
            return self.awrRepository.getAwrHtml(dbid, begin_snap, end_snap)
        except Exception as ex:
            self._logger.error (f"get AwrHtml error: {ex}")
            

    def dropAwr(self,dbid: int64, begin_snap: int32, end_snap:int32)-> bool:
        '''Drop Awr
        
        :return: True when drop successful, otherwise return False'''
        return self.awrRepository.dropAwr(dbid, begin_snap, end_snap)
    
    def getAwrRepositoryInfo(self):
        return self.awrRepository.getAwrRepositoryInfo()
    
