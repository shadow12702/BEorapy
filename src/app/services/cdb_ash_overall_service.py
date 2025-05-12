# Description: CdbService

import pandas as pd
from numpy import int64
from app.factory import ApplicationFactory
from utils.multi_threads import MultiThreads
from dependencies import config_manager as cf_manager
from logger import AppLogger
from app.models.responses.cdb.cdb_response import AshOverallMetricResponse, AshOverallObjectMetricResponse

class CdbAshOverallService():
    
    CSV_OUTPUT_PATH:str = "staging/cdb"
    _logger = AppLogger().get_logger()
    
    def __init__(self, factory: ApplicationFactory, max_threads:int = cf_manager.app_config.MaxThread):
        self._repository = factory.cdb_ash_overall_repository()        
        self._multiThreads = MultiThreads(max_threads)

    async def get_ash_overall_metric(self, metric_type:str, cus_code: str,  dbid:int64, begin_snap: int, end_snap: int):
        _overalls = await self.repository.ash_overall_metric(metric_type, cus_code, dbid, begin_snap, end_snap)
        result = [AshOverallMetricResponse.from_model(item) for item in _overalls]
        return result
    
    async def get_ash_overall_object_metric(self, metric_type:str, cus_code: str,  dbid:int64, begin_snap: int, end_snap: int):
        _overall_objects = await self.repository.ash_overall_object_metric(metric_type, cus_code, dbid, begin_snap, end_snap)
        result = [AshOverallObjectMetricResponse.from_model(item) for item in _overall_objects]
        return result
    
    async def get_ash_overall_segment(self, cus_code: str,  dbid:int64):
        begin_snap = 731
        end_snap = 927
        data = await self.repository.ash_overall_segment(cus_code, dbid, begin_snap, end_snap)
        return data
    
    " ----------------========="
    async def get_ash_overall_wait_class(self, cus_code: str,  dbid:int64):
        begin_snap = 731
        end_snap = 927
        data = await self.repository.ash_overall_wait_class(cus_code, dbid, begin_snap, end_snap)
        
        return data
    
    async def get_ash_overall_event(self, cus_code: str,  dbid:int64):
        begin_snap = 731
        end_snap = 927
        data = await self.repository.ash_overall_event(cus_code, dbid, begin_snap, end_snap)
        return data
    
    async def get_ash_overall_module(self, cus_code: str,  dbid:int64):
        begin_snap = 731
        end_snap = 927
        data = await self.repository.ash_overall_module(cus_code, dbid, begin_snap, end_snap)
        return data
    
    async def get_ash_overall_program(self, cus_code: str,  dbid:int64):
        begin_snap = 731
        end_snap = 927
        data = await self.repository.ash_overall_program(cus_code, dbid, begin_snap, end_snap)
        return data
    
    async def get_ash_overall_sql_cpu(self, cus_code: str,  dbid:int64):
        begin_snap = 731
        end_snap = 927
        data = await self.repository.ash_overall_sql_cpu(cus_code, dbid, begin_snap, end_snap)
        return data
    
    async def get_ash_overall_sql_io(self, cus_code: str,  dbid:int64):
        begin_snap = 731
        end_snap = 927
        data = await self.repository.ash_overall_sql_io(cus_code, dbid, begin_snap, end_snap)
        return data

    async def get_ash_overall_sql_operation(self, cus_code: str,  dbid:int64):
        begin_snap = 731
        end_snap = 927
        data = await self.repository.ash_overall_sql_operation(cus_code, dbid, begin_snap, end_snap)
        return data
    
    async def get_ash_overall_wait(self, cus_code: str,  dbid:int64):
        begin_snap = 731
        end_snap = 927
        data = await self.repository.ash_overall_wait(cus_code, dbid, begin_snap, end_snap)
        return data
    
    async def get_ash_overall_wait_global(self, cus_code: str,  dbid:int64):
        begin_snap = 731
        end_snap = 927
        data = await self.repository.ash_overall_wait_global(cus_code, dbid, begin_snap, end_snap)
        return data
    " ----------------========="

    @property
    def repository(self):
        return self._repository        
    
    @property
    def multiThreads(self):
        return self._multiThreads
    
    def extract_top_sql(self, top_n_rows:int=10):        
        try:
            functions = [
                ('getExtractTopSqlCpu',[top_n_rows], {}),
                ('getExtractTopSqlWait',[top_n_rows], {}),
                ('getExtractTopSqlIo',[top_n_rows], {}),        
            ]
            self.processing(functions)
        except Exception as ex:
            self._logger.error(f"Extract top SQL failed. \nError: {ex}")
        
    
    def executing(self, dbid:int64, begin_snap:int64, end_snap:int64):
        try:
            functions = [                
               
                ('getDbTopSqlSnapLogicalRead',[dbid, begin_snap, end_snap], {}),
                ('getDbTopSqlSnapDiskReads',[dbid, begin_snap, end_snap], {}),
                ('getDbTopSqlSnapPhysicalReadIops',[dbid, begin_snap, end_snap], {}),
                ('getDbTopSqlSnapPhysicalWriteIops',[dbid, begin_snap, end_snap], {}),
                ('getDbTopSqlSnapPhysicalWriteDirIops',[dbid, begin_snap, end_snap], {}),
                ('getDbTopSqlSnapInvalid',[dbid, begin_snap, end_snap], {}),
            ]            
            self.processing(functions)
        except Exception as ex:
            self._logger.error(f"Executing query for healthcheck failed. \nError: {ex}")
        