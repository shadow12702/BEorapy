# Description: CdbService

import pandas as pd
from numpy import int64
from app.factory import ApplicationFactory
from services.db_service import DbService
from utils.multi_threads import MultiThreads
from core.config.app_setting import cff_loader
from logger import AppLogger

class CdbService(DbService):
    
    CSV_OUTPUT_PATH:str = "staging/cdb"
    _logger = AppLogger().get_logger()
    
    def __init__(self, repo_factory: ApplicationFactory, max_threads:int = cff_loader.appConfig.MaxThread):        
        self._cdbRepository = repo_factory.cdbRepository()        
        self._multiThreads = MultiThreads(max_threads)

    def getService(self,  dbid:int64, begin_snap:int64, end_snap:int64):
        data =self._cdbRepository.getMemResize(dbid, begin_snap, end_snap)
        print(data)
        return data

    def getDbInfo(self, dbid:int64):
        value = self._cdbRepository.getDbInfo(dbid)
        data = [d.__dict__ for d in value]
        df= pd.DataFrame(data)
        df.to_csv(f"{CdbService.CSV_OUTPUT_PATH}/db_info.csv", index=False)
    
    @property
    def repository(self):
        return self._cdbRepository        
    
    @property
    def multiThreads(self):
        return self._multiThreads
    
    def extractTopSql(self, top_n_rows:int=10):        
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
                ('getDbaHistoryStatistic',[dbid, begin_snap, end_snap], {}),
                ('getDbaHistoryStatisticGlobal',[dbid, begin_snap, end_snap], {}),
                ('getSqlPlanChange',[dbid, begin_snap, end_snap], {}),
                ('getMemResize',[dbid, begin_snap, end_snap], {}),
                ('getAshOverallSegment',[dbid, begin_snap, end_snap], {}),
                ('getAshOverallIndex',[dbid, begin_snap, end_snap], {}),
                ('getAshOverallTable',[dbid, begin_snap, end_snap], {}),
                ('getAshOverallWaitClass',[dbid, begin_snap, end_snap], {}),
                ('getAshOverallEvent',[dbid, begin_snap, end_snap], {}),
                ('getAshOverallModule',[dbid, begin_snap, end_snap], {}),
                ('getAshOverallProgram',[dbid, begin_snap, end_snap], {}),
                ('getAshOverallSqlCpu',[dbid, begin_snap, end_snap], {}),
                ('getAshOverallSqlIo',[dbid, begin_snap, end_snap], {}),
                ('getAshOverallSqlWait',[dbid, begin_snap, end_snap], {}),
                ('getAshOverallSqlOperation',[dbid, begin_snap, end_snap], {}),
                ('getAshOverallWait',[dbid, begin_snap, end_snap], {}),
                ('getAshOverallWaitGlobal',[dbid, begin_snap, end_snap], {}),
                ('getIoFileTypeStatisticGlobal',[dbid, begin_snap, end_snap], {}),
                ('getLatchStatistic',[dbid, begin_snap, end_snap], {}),
                ('getLibraryCacheStatistic',[dbid, begin_snap, end_snap], {}),
                ('getOsStatistic',[dbid, begin_snap, end_snap], {}),
                ('getGcBlockSrvGraph',[dbid, begin_snap, end_snap], {}),
                ('getIoFunctionStatistic',[dbid, begin_snap, end_snap], {}),
                ('getIoFunctionStatisticGlobal',[dbid, begin_snap, end_snap], {}),
                ('getPgaEffStatistic',[dbid, begin_snap, end_snap], {}),
                ('getTimeModelStatistic',[dbid, begin_snap, end_snap], {}),
                ('getSgaStatistic',[dbid, begin_snap, end_snap], {}),
                ('getSgaPdbStatistic',[dbid, begin_snap, end_snap], {}),
                ('getGcEfficientGraph',[dbid, begin_snap, end_snap], {}),
                ('getMemConfig',[dbid, begin_snap, end_snap], {}),
                ('getBufferPoolConfig',[dbid, begin_snap, end_snap], {}),
                ('getMetricStatistic',[dbid, begin_snap, end_snap], {}),
                ('getGcLoadProfile',[dbid, begin_snap, end_snap], {}),
                ('getUndoConfig',[dbid, begin_snap, end_snap], {}),
                ('getTbsIoStatistic',[dbid, begin_snap, end_snap], {}),
                ('getGcWorkload',[dbid, begin_snap, end_snap], {}),
                ('getGcEnqueueMessaging',[dbid, begin_snap, end_snap], {}),
                ('getPdbMetric',[dbid, begin_snap, end_snap], {}),
                ('getDbSqlFullScan',[dbid, begin_snap, end_snap], {}),
                ('getDbWeAas',[dbid, begin_snap, end_snap], {}),
                ('getAwrAasGraphGlobal',[dbid, begin_snap, end_snap], {}),
                ('getAwrAasGraph',[dbid, begin_snap, end_snap], {}),
                ('getIoFileTypeStatistic',[dbid, begin_snap, end_snap], {}),
                ('getPgaStatistic',[dbid, begin_snap, end_snap], {}),
                ('getResourceLimit',[dbid, begin_snap, end_snap], {}),
                ('getDbWcAas',[dbid, begin_snap, end_snap], {}),                
                ('getExaCellServerIoStatistic',[dbid, begin_snap, end_snap], {}),
                ('getExaCellServerIoStatisticCell',[dbid, begin_snap, end_snap], {}),
                ('getExaTopDatabaseIoStatistic',[dbid, begin_snap, end_snap], {}),
                ('getExaDatabaseSystat',[dbid, begin_snap, end_snap], {}),
                ('getExaCellSummary',[dbid, begin_snap, end_snap], {}),
                ('getExaCellGlobalCell',[dbid, begin_snap, end_snap], {}),
                ('getExaCellGlobal',[dbid, begin_snap, end_snap], {}),
                ('getExaIoReason',[dbid, begin_snap, end_snap], {}),
                ('getExaCellAlert',[dbid, begin_snap, end_snap], {}),
                ('getExaAsmDiskgroup',[dbid, begin_snap, end_snap], {}),
                ('getAshCpuWaitAnalysicReport',[dbid, begin_snap, end_snap], {}),
                ('getAshTopEventBySnap',[dbid, begin_snap, end_snap], {}),
                ('getAshSqlEventBySnap',[dbid, begin_snap, end_snap], {}),
                ('getAshTopSegmentBySnap',[dbid, begin_snap, end_snap], {}),
                ('getAshTopSegmentEventBySnap',[dbid, begin_snap, end_snap], {}),
                ('getAshTopSegmentSqlEventBySnap',[dbid, begin_snap, end_snap], {}),
                ('getAshSqlPlanEventBySnap',[dbid, begin_snap, end_snap], {}),
                ('getAshTopSqlCostBySnap',[dbid, begin_snap, end_snap], {}),
                ('getAshTopEventBackground',[dbid, begin_snap, end_snap], {}),
                ('getAshTopEventNotBackground',[dbid, begin_snap, end_snap], {}),
                ('getAshEventObjForeground',[dbid, begin_snap, end_snap], {}),
                ('getAshEventObjForegroundByDb',[dbid, begin_snap, end_snap], {}),
                ('getAshEventGc',[dbid, begin_snap, end_snap], {}),
                ('getAshEventGcByDb',[dbid, begin_snap, end_snap], {}),
                ('getAshEventEnq',[dbid, begin_snap, end_snap], {}),
                ('getAshEventEnqByDb',[dbid, begin_snap, end_snap], {}),
                ('getAshEventLatch',[dbid, begin_snap, end_snap], {}),
                ('getAshEventLatchByDb',[dbid, begin_snap, end_snap], {}),
                ('getAshEventDirect',[dbid, begin_snap, end_snap], {}),
                ('getAshEventDirectByDb',[dbid, begin_snap, end_snap], {}),
                ('getAshEventDbfile',[dbid, begin_snap, end_snap], {}),
                ('getAshEventDbfileByDb',[dbid, begin_snap, end_snap], {}),
                ('getAshEventCell',[dbid, begin_snap, end_snap], {}),
                ('getAshEventCellByDb',[dbid, begin_snap, end_snap], {}),
                ('getAshEventRowlock',[dbid, begin_snap, end_snap], {}),
                ('getAshEventItl',[dbid, begin_snap, end_snap], {}),
                ('getAshEventIndexContention',[dbid, begin_snap, end_snap], {}),
                ('getAshEventBufferBusy',[dbid, begin_snap, end_snap], {}),
                ('getAshEventHwContention',[dbid, begin_snap, end_snap], {}),
                ('getAshSqlIdEvent',[dbid, begin_snap, end_snap], {}),
                ('getAshSqlIdSqContention',[dbid, begin_snap, end_snap], {}),
                ('getAshSqlIdCursor',[dbid, begin_snap, end_snap], {}),
                ('getAshSqlIdRowcache',[dbid, begin_snap, end_snap], {}),
                ('getAshSqlIdIoWaits',[dbid, begin_snap, end_snap], {}),
                ('getAshSqlPlanChange',[dbid, begin_snap, end_snap], {}),
                ('getAshWaitClass',[dbid, begin_snap, end_snap], {}),
                ('getDbTopSegmentTableScans',[dbid, begin_snap, end_snap], {}),
                ('getDbTopSegmentPhysicalWriteIops',[dbid, begin_snap, end_snap], {}),
                ('getDbTopSegmentPhysicalWriteDir',[dbid, begin_snap, end_snap], {}),
                ('getDbTopSegmentRowLock',[dbid, begin_snap, end_snap], {}),
                ('getDbTopSegmentPhysicalWrite',[dbid, begin_snap, end_snap], {}),
                ('getDbTopSegmentPhysicalReadIops',[dbid, begin_snap, end_snap], {}),
                ('getDbTopSegmentPhysicalReadDir',[dbid, begin_snap, end_snap], {}),
                ('getDbTopSegmentPhysicalRead',[dbid, begin_snap, end_snap], {}),
                ('getDbTopSegmentOptPhysicalRead',[dbid, begin_snap, end_snap], {}),
                ('getDbTopSegmentLogicalRead',[dbid, begin_snap, end_snap], {}),
                ('getDbTopSegmentItlWaits',[dbid, begin_snap, end_snap], {}),
                ('getDbTopSegmentGcCurrentBlockSrv',[dbid, begin_snap, end_snap], {}),
                ('getDbTopSegmentGcCurrentBlockRec',[dbid, begin_snap, end_snap], {}),
                ('getDbTopSegmentGcCrBlockSrv',[dbid, begin_snap, end_snap], {}),
                ('getDbTopSegmentGcCrBlockRec',[dbid, begin_snap, end_snap], {}),
                ('getDbTopSegmentGcBufferBusyWait',[dbid, begin_snap, end_snap], {}),
                ('getDbTopSegmentChainRow',[dbid, begin_snap, end_snap], {}),
                ('getDbTopSegmentBufferBusyWait',[dbid, begin_snap, end_snap], {}),
                ('getDbTopSegmentBlockChange',[dbid, begin_snap, end_snap], {}),
                ('getDbTopSegmentSnapTableScans',[dbid, begin_snap, end_snap], {}),
                ('getDbTopSegmentSnapPhysicalWriteIops',[dbid, begin_snap, end_snap], {}),
                ('getDbTopSegmentSnapPhysicalWriteDir',[dbid, begin_snap, end_snap], {}),
                ('getDbTopSegmentSnapRowLock',[dbid, begin_snap, end_snap], {}),
                ('getDbTopSegmentSnapPhysicalWrite',[dbid, begin_snap, end_snap], {}),
                ('getDbTopSegmentSnapPhysicalReadIops',[dbid, begin_snap, end_snap], {}),
                ('getDbTopSegmentSnapPhysicalReadDir',[dbid, begin_snap, end_snap], {}),
                ('getDbTopSegmentSnapPhysicalRead',[dbid, begin_snap, end_snap], {}),
                ('getDbTopSegmentSnapOptPhysicalRead',[dbid, begin_snap, end_snap], {}),
                ('getDbTopSegmentSnapLogicalRead',[dbid, begin_snap, end_snap], {}),
                ('getDbTopSegmentSnapItlWaits',[dbid, begin_snap, end_snap], {}),
                ('getDbTopSegmentSnapGcCurrentBlockSrv',[dbid, begin_snap, end_snap], {}),
                ('getDbTopSegmentSnapGcCurrentBlockRec',[dbid, begin_snap, end_snap], {}),
                ('getDbTopSegmentSnapGcCrBlockSrv',[dbid, begin_snap, end_snap], {}),
                ('getDbTopSegmentSnapGcCrBlockRec',[dbid, begin_snap, end_snap], {}),
                ('getDbTopSegmentSnapGcBufferBusyWait',[dbid, begin_snap, end_snap], {}),
                ('getDbTopSegmentSnapChainRow',[dbid, begin_snap, end_snap], {}),
                ('getDbTopSegmentSnapBufferBusyWait',[dbid, begin_snap, end_snap], {}),
                ('getDbTopSegmentSnapBlockChange',[dbid, begin_snap, end_snap], {}),
                ('getDbTopSqlTotalExec',[dbid, begin_snap, end_snap], {}),
                ('getDbTopSqlVersions',[dbid, begin_snap, end_snap], {}),
                ('getDbTopSqlOffLoadReturn',[dbid, begin_snap, end_snap], {}),
                ('getDbTopSqlOffLoad',[dbid, begin_snap, end_snap], {}),
                ('getDbTopSqlPhysicalWriteMb',[dbid, begin_snap, end_snap], {}),
                ('getDbTopSqlPhysicalReadMb',[dbid, begin_snap, end_snap], {}),
                ('getDbTopSqlParseCall',[dbid, begin_snap, end_snap], {}),
                ('getDbTopSqlCpu',[dbid, begin_snap, end_snap], {}),
                ('getDbTopSqlIoWait',[dbid, begin_snap, end_snap], {}),
                ('getDbTopSqlCwait',[dbid, begin_snap, end_snap], {}),
                ('getDbTopSqlCcWait',[dbid, begin_snap, end_snap], {}),
                ('getDbTopSqlAppWait',[dbid, begin_snap, end_snap], {}),
                ('getDbTopSqlElapsed',[dbid, begin_snap, end_snap], {}),
                ('getDbTopSqlLogicalRead',[dbid, begin_snap, end_snap], {}),
                ('getDbTopSqlDiskReads',[dbid, begin_snap, end_snap], {}),
                ('getDbTopSqlPhysicalReadIops',[dbid, begin_snap, end_snap], {}),
                ('getDbTopSqlPhysicalWriteIops',[dbid, begin_snap, end_snap], {}),
                ('getDbTopSqlPhysicalWriteDirIops',[dbid, begin_snap, end_snap], {}),
                ('getDbTopSqlSnapTotalExec',[dbid, begin_snap, end_snap], {}),
                ('getDbTopSqlSnapVersions',[dbid, begin_snap, end_snap], {}),
                ('getDbTopSqlSnapOffLoadReturn',[dbid, begin_snap, end_snap], {}),
                ('getDbTopSqlSnapOffLoad',[dbid, begin_snap, end_snap], {}),
                ('getDbTopSqlSnapPhysicalWriteMb',[dbid, begin_snap, end_snap], {}),
                ('getDbTopSqlSnapPhysicalReadMb',[dbid, begin_snap, end_snap], {}),
                ('getDbTopSqlSnapParseCall',[dbid, begin_snap, end_snap], {}),
                ('getDbTopSqlSnapCpu',[dbid, begin_snap, end_snap], {}),
                ('getDbTopSqlSnapIowait',[dbid, begin_snap, end_snap], {}),
                ('getDbTopSqlSnapCwait',[dbid, begin_snap, end_snap], {}),
                ('getDbTopSqlSnapCcWait',[dbid, begin_snap, end_snap], {}),
                ('getDbTopSqlSnapAppWait',[dbid, begin_snap, end_snap], {}),
                ('getDbTopSqlSnapElapsed',[dbid, begin_snap, end_snap], {}),
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
        