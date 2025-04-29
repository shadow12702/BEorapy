from numpy import int32, int64
from typing import List
from data.db_context import DbContext, DataOperators
from app.data.repositories.general_repository import GeneralRepository
from app.data.entities.awr import Awr
from app.data.entities.awr_html import AwrHtml
from app.data.entities.awr_config import AwrConfig
from app.data.entities.awr_healthcheck import AwrHealthcheck
from app.data.repositories.enum.awr_enum import AwrEnum
from logger import AppLogger


class AwrRepository(GeneralRepository):

    _logger = AppLogger().get_logger()
    
    def __init__(self, db_context: DbContext):
        
        if not isinstance(db_context, DataOperators):
            self._logger.error(TypeError("db_context must implement DataOperations"))        
        self.db_context = db_context
        
    
    def getAwrRepositoryInfo(self):
        '''Get list AWRs
        
        :return: list of AWRs
        '''
        try:
            plsql = self.redis.getKey(AwrEnum.AWR_REPOSITORY_INFO.value)            
            data = self.db_context.callPlSql(plsql)
            awrs = [Awr(**awr) for awr in data] if data else [Awr.empty()]
            return awrs
        except Exception as ex:
            self._logger.error(f"Get Awrs error: {ex}")
        
    def getAwrConfig(self, dbid: int64, begin_snap: int32, end_snap: int32):
        '''
        Get AWR configuration
        
        :return: AWR Config information'''
        return self.getValue(AwrEnum.AWR_GL_CONFIG, AwrConfig, dbid, begin_snap, end_snap)
        
            
    def getAwrsForOutputHtml(self, dbid:int64, begin_snap: int32, end_snap: int32):
        ''':return: list of AwrHtml
        '''
        return self.getValue(AwrEnum.ALL_AWRS_FOR_OUTPUT_HTML, AwrHtml, dbid, begin_snap, end_snap)
        # try:            
        #     query = self.redis.getKey(AwrEnum.ALL_AWRS_FOR_OUTPUT_HTML.value)
        #     data = self.db_context.getData(query=query,
        #                                    params={'P_DBID': dbid,                                                    
        #                                            "P_BEGIN_SNAP":begin_snap, 
        #                                            "P_END_SNAP":end_snap                                                   
        #                                            })
        #     awrHtml = [AwrHtml(**html) for html in data] if data else List[AwrHtml.empty()]
        #     return awrHtml
        # except Exception as ex:
        #     self._logger.error(f"Get AwrForHealthCheck error: {ex}")

    def getAwrOutputToHtml(self, dbid:int64, instance_no:int, begin_snap: int32, end_snap: int32):
        ''':return: list of AwrHtml
        '''
        try:            
            query = self.redis.getKey(AwrEnum.OUTPUT_AWR_TO_HTML.value)
            data = self.db_context.getData(query=query,
                                           params={'P_DBID': dbid, 
                                                   'P_INSTANCE_NO': instance_no,
                                                   "P_BEGIN_SNAP":begin_snap, 
                                                   "P_END_SNAP":end_snap})
            awrHtml = [AwrHtml(**html) for html in data] if data else List[AwrHtml.empty()]
            return awrHtml
        except Exception as ex:
            self._logger.error(f"Get AwrForHealthCheck error: {ex}")

    def dropAwr(self, dbid:int64, begin_snap: int32, end_snap: int32) -> bool:
        '''Drop Awr
        
        :return: True when drop successful, otherwise return False'''
        try:
            query = self.redis.getKey(AwrEnum.DROP_AWR.value)
            self.db_context.getData(query=query,
                                    params={'P_DBID': dbid, 
                                            "P_BEGIN_SNAP":begin_snap, 
                                            "P_END_SNAP":end_snap})
            return True
        except Exception as ex:
            self._logger.error(f"dropAwr error: {ex}")
            return False


    def getAwrsForHealthcheck(self):
        '''
        Get AWRs for healthcheck
        
        :return: list of AwrHealthcheck'''
        try:
            # data = self.db_context.callFunction(func_name=f"{OrapyPackage.AWRS.value}.FN_GET_AWRS_HEALTHCHECK", 
                                                #  return_type= OracleDataType.CURSOR.value)
            query = self.redis.getKey(AwrEnum.AWRS_FOR_HEALTHCHECK.value)
            data = self.db_context.getData(query=query) 
            awrHc = [AwrHealthcheck(**hc) for hc in data] if data else List[AwrHealthcheck.empty()]
            return awrHc
        except Exception as ex:
            self._logger.error(f"Get AwrForHealthCheck error: {ex}")

        