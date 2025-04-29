from numpy import int32, int64
from data.db_context import DbContext, DataOperators
from app.data.repositories.general_repository import GeneralRepository
from logger import AppLogger
from app.data.repositories.enum.cdb_enum import CdbEnum
from app.data.entities.cdb_models import *
from app.data.models.cdb_model import *

    
class CdbRepository(GeneralRepository):
    
    _logger = AppLogger().get_logger()
    
    def __init__(self, db_context: DbContext):
        
        if not isinstance(db_context, DataOperators):
            self._logger.error(TypeError("db_context must implement DataOperations"))        
        self.db_context = db_context
    

    def getDbaHistoryStatistic(self, dbid:int64, begin_snap: int32, end_snap: int32):
        return self.getValue(CdbEnum.DBA_HISTORY_STATISTIC, CdbDbaHistoryStatistic, 
                             dbid, begin_snap, end_snap)

    def getDbaHistoryStatisticGlobal(self, dbid:int64, begin_snap: int32, end_snap: int32):
        return self.getValue(CdbEnum.DBA_HISTORY_STATISTIC_GLOBAL, CdbDbaHistoryStatisticGlobal, 
                             dbid, begin_snap, end_snap)

    def getSqlPlanChange(self, dbid:int64, begin_snap: int32, end_snap: int32):
        return self.getValue(CdbEnum.SQL_PLAN_CHANGE, CdbSqlPlanChange, 
                             dbid, begin_snap, end_snap)
    
    def getMemResize(self, dbid:int64, begin_snap: int32, end_snap: int32):
        return self.getValue(CdbEnum.MEM_RESIZE, CdbMemResize, 
                             dbid, begin_snap, end_snap)
         
    def getAshOverallSegment(self, dbid:int64, begin_snap: int32, end_snap: int32):
        return self.getValue(CdbEnum.ASH_OVERALL_SEGMENT, CdbAshOverallSegment, 
                             dbid, begin_snap, end_snap)
         
    def getAshOverallIndex(self, dbid:int64, begin_snap: int32, end_snap: int32):
        return self.getValue(CdbEnum.ASH_OVERALL_INDEX, CdbAshOverallIndex, 
                             dbid, begin_snap, end_snap)
         
    def getAshOverallTable(self, dbid:int64, begin_snap: int32, end_snap: int32):
        return self.getValue(CdbEnum.ASH_OVERALL_TABLE, CdbAshOverallTable, 
                             dbid, begin_snap, end_snap)
        
    def getAshOverallWaitClass(self, dbid:int64, begin_snap: int32, end_snap: int32):
        return self.getValue(CdbEnum.ASH_OVERALL_WAIT_CLASS, CdbAshOverallWaitClass, 
                             dbid, begin_snap, end_snap)
    
    def getAshOverallEvent(self, dbid:int64, begin_snap: int32, end_snap: int32):
        return self.getValue(CdbEnum.ASH_OVERALL_EVENT, CdbAshOverallEvent, 
                            dbid, begin_snap, end_snap)    
    
    def getAshOverallModule(self, dbid:int64, begin_snap: int32, end_snap: int32):
        return self.getValue(CdbEnum.ASH_OVERALL_MODULE, CdbAshOverallModule, 
                            dbid, begin_snap, end_snap)
    
    def getAshOverallProgram(self, dbid:int64, begin_snap: int32, end_snap: int32):
        return self.getValue(CdbEnum.ASH_OVERALL_PROGRAM, CdbAshOverallProgram, 
                            dbid, begin_snap, end_snap)
    
    def getAshOverallSqlCpu(self, dbid:int64, begin_snap: int32, end_snap: int32):
        return self.getValue(CdbEnum.ASH_OVERALL_SQL_CPU, CdbAshOverallSqlCpu, 
                            dbid, begin_snap, end_snap)
        
    def getAshOverallSqlIo(self, dbid:int64, begin_snap: int32, end_snap: int32):
        return self.getValue(CdbEnum.ASH_OVERALL_SQL_IO, CdbAshOverallSqlIo, 
                            dbid, begin_snap, end_snap)
        
    def getAshOverallSqlWait(self, dbid:int64, begin_snap: int32, end_snap: int32):
        return self.getValue(CdbEnum.ASH_OVERALL_SQL_CPU, CdbAshOverallSqlWait, 
                            dbid, begin_snap, end_snap)
         
    def getAshOverallSqlOperation(self, dbid:int64, begin_snap: int32, end_snap: int32):
        return self.getValue(CdbEnum.ASH_OVERALL_SQL_OPERATION, CdbAshOverallSqlOperation,
                            dbid, begin_snap, end_snap)
         
    def getAshOverallWait(self, dbid:int64, begin_snap: int32, end_snap: int32):
        return self.getValue(CdbEnum.ASH_OVERALL_WAIT, CdbAshOverallWait, 
                            dbid, begin_snap, end_snap)
         
    def getAshOverallWaitGlobal(self, dbid:int64, begin_snap: int32, end_snap: int32):
        return self.getValue(CdbEnum.ASH_OVERALL_WAIT_GLOBAL, CdbAshOverallWaitGlobal, 
                            dbid, begin_snap, end_snap)
    
    def getIoFileTypeStatisticGlobal(self, dbid:int64, begin_snap: int32, end_snap: int32):
        return self.getValue(CdbEnum.IO_FILE_TYPE_STATISTIC_GLOBAL, CdbIoFileTypeStatisticGlobal, 
                            dbid, begin_snap, end_snap)
    
    def getLatchStatistic(self, dbid:int64, begin_snap: int32, end_snap: int32):
        return self.getValue(CdbEnum.LATCH_STATISTIC, CdbLatchStatistic, 
                            dbid, begin_snap, end_snap)
    
    def getLibraryCacheStatistic(self, dbid:int64, begin_snap: int32, end_snap: int32):
        return self.getValue(CdbEnum.LIBRARY_CACHE_STATISTIC, CdbLibraryCacheStatistic, 
                            dbid, begin_snap, end_snap)
    
    def getOsStatistic(self, dbid:int64, begin_snap: int32, end_snap: int32):
        return self.getValue(CdbEnum.OS_STATISTIC, OdbOsStatistic, 
                            dbid, begin_snap, end_snap)
    
    def getGcBlockSrvGraph(self, dbid:int64, begin_snap: int32, end_snap: int32):
        return self.getValue(CdbEnum.GC_BLOCK_SRV_GRAPH, OdbGcBlockSrvGraph, 
                            dbid, begin_snap, end_snap)
    
    def getIoFunctionStatistic(self, dbid:int64, begin_snap: int32, end_snap: int32):
        return self.getValue(CdbEnum.IO_FUNCTION_STATISTIC, OdbIoFunctionStatistic, 
                            dbid, begin_snap, end_snap)
    
    def getIoFunctionStatisticGlobal(self, dbid:int64, begin_snap: int32, end_snap: int32):
        return self.getValue(CdbEnum.IO_FUNCTION_STATISTIC_GLOBAL, OdbIoFunctionStatisticGlobal, 
                            dbid, begin_snap, end_snap)
    
    def getPgaEffStatistic(self, dbid:int64, begin_snap: int32, end_snap: int32):
        return self.getValue(CdbEnum.PGA_EFF_STATISTIC, OdbPgaEffStatistic, 
                            dbid, begin_snap, end_snap)
    
    def getTimeModelStatistic(self, dbid:int64, begin_snap: int32, end_snap: int32):
        return self.getValue(CdbEnum.TIME_MODEL_STATISTIC, OdbTimeModelStatistic, 
                            dbid, begin_snap, end_snap)
    
    def getSgaStatistic(self, dbid:int64, begin_snap: int32, end_snap: int32):
        return self.getValue(CdbEnum.SGA_STATISTIC, OdbSgaStatistic, 
                            dbid, begin_snap, end_snap)
    
    def getSgaPdbStatistic(self, dbid:int64, begin_snap: int32, end_snap: int32):
        return self.getValue(CdbEnum.SGA_PDB_STATISTIC, CdbSgaPdbStatistic, 
                            dbid, begin_snap, end_snap)

    def getGcEfficientGraph(self, dbid:int64, begin_snap: int32, end_snap: int32):
        return self.getValue(CdbEnum.GC_EFFICIENT_GRAPH, OdbGcEfficientGraph, 
                            dbid, begin_snap, end_snap)
     
    def getMemConfig(self, dbid:int64, begin_snap: int32, end_snap: int32):
        return self.getValue(CdbEnum.MEM_CONFIG, OdbMemConfig, 
                            dbid, begin_snap, end_snap)
    
    def getBufferPoolConfig(self, dbid:int64, begin_snap: int32, end_snap: int32):
        return self.getValue(CdbEnum.BUFFER_POOL_CONFIG, OdbBufferPoolConfig, 
                            dbid, begin_snap, end_snap)
    
    def getMetricStatistic(self, dbid:int64, begin_snap: int32, end_snap: int32):
        return self.getValue(CdbEnum.METRIC_STATISTIC, OdbMetricStatistic, 
                            dbid, begin_snap, end_snap)
    
    def getGcLoadProfile(self, dbid:int64, begin_snap: int32, end_snap: int32):
        return self.getValue(CdbEnum.GC_LOAD_PROFILE, OdbGcLoadProfile, 
                            dbid, begin_snap, end_snap)
    
    def getUndoConfig(self, dbid:int64, begin_snap: int32, end_snap: int32):
        return self.getValue(CdbEnum.UNDO_CONFIG, OdbUndoConfig, 
                            dbid, begin_snap, end_snap)
    
    def getTbsIoStatistic(self, dbid:int64, begin_snap: int32, end_snap: int32):
        return self.getValue(CdbEnum.TBS_IO_STATISTIC, OdbTbsIoStatistic, 
                            dbid, begin_snap, end_snap)
    
    def getGcWorkload(self, dbid:int64, begin_snap: int32, end_snap: int32):
        return self.getValue(CdbEnum.GC_WORKLOAD, OdbGcWorkload, 
                            dbid, begin_snap, end_snap)
    
    def getGcEnqueueMessaging(self, dbid:int64, begin_snap: int32, end_snap: int32):
        return self.getValue(CdbEnum.GC_ENQUEUE_MESSAGING, OdbGcEnqueueMessaging, 
                            dbid, begin_snap, end_snap)
    
    def getPdbMetric(self, dbid:int64, begin_snap: int32, end_snap: int32):
        return self.getValue(CdbEnum.PDB_METRIC, CdbPdbMetric, 
                            dbid, begin_snap, end_snap)
    
     
    def getDbSqlFullScan(self, dbid:int64, begin_snap: int32, end_snap: int32):
        return self.getValue(CdbEnum.DB_SQL_FULL_SCAN, CdbSqlFullScan, 
                            dbid, begin_snap, end_snap)
    
    def getDbWeAas(self, dbid:int64, begin_snap: int32, end_snap: int32):
        return self.getValue(CdbEnum.DB_WE_AAS, OdbDbWeAas, 
                            dbid, begin_snap, end_snap)
    
    def getAwrAasGraphGlobal(self, dbid:int64, begin_snap: int32, end_snap: int32):
        return self.getValue(CdbEnum.AWR_AAS_GRAPH_GLOBAL, OdbAwrAasGraphGlobal, 
                            dbid, begin_snap, end_snap)
    
    def getAwrAasGraph(self, dbid:int64, begin_snap: int32, end_snap: int32):
        return self.getValue(CdbEnum.AWR_AAS_GRAPH, OdbAwrAasGraph, 
                            dbid, begin_snap, end_snap)
    
    def getIoFileTypeStatistic(self, dbid:int64, begin_snap: int32, end_snap: int32):
        return self.getValue(CdbEnum.IO_FILE_TYPE_STATISTIC, CdbIoFileTypeStatistic, 
                            dbid, begin_snap, end_snap)
    
    def getPgaStatistic(self, dbid:int64, begin_snap: int32, end_snap: int32):
        return self.getValue(CdbEnum.PGA_STATISTIC, OdbPgaStatistic, 
                            dbid, begin_snap, end_snap)
    
    def getResourceLimit(self, dbid:int64, begin_snap: int32, end_snap: int32):
        return self.getValue(CdbEnum.RESOURCE_LIMIT, OdbResourceLimit, 
                            dbid, begin_snap, end_snap)
    
    def getDbWcAas(self, dbid:int64, begin_snap: int32, end_snap: int32):
        return self.getValue(CdbEnum.DB_WC_AAS, OdbDbWcAas, 
                            dbid, begin_snap, end_snap)
        
    def getExaCellServerIoStatistic(self, dbid:int64, begin_snap: int32, end_snap: int32):
        return self.getValue(CdbEnum.EXA_CELL_SERVER_IO_STATISTIC, OdbExaCellServerIoStatistic, 
                            dbid, begin_snap, end_snap)
    
    def getExaCellServerIoStatisticCell(self, dbid:int64, begin_snap: int32, end_snap: int32):
        return self.getValue(CdbEnum.EXA_CELL_SERVER_IO_STATISTIC_CELL, OdbExaCellServerIoStatisticCell, 
                            dbid, begin_snap, end_snap)
    
    def getExaTopDatabaseIoStatistic(self, dbid:int64, begin_snap: int32, end_snap: int32):
        return self.getValue(CdbEnum.EXA_TOP_DATABASE_IO_STATISTIC, OdbExaTopDatabaseIoStatistic, 
                            dbid, begin_snap, end_snap)
    
    def getExaDatabaseSystat(self, dbid:int64, begin_snap: int32, end_snap: int32):
        return self.getValue(CdbEnum.EXA_DATABASE_SYSTAT, OdbExaDatabaseSystat, 
                            dbid, begin_snap, end_snap)
    
    def getExaCellSummary(self, dbid:int64, begin_snap: int32, end_snap: int32):
        return self.getValue(CdbEnum.EXA_CELL_SUMMARY, OdbExaCellSummary, 
                            dbid, begin_snap, end_snap)
    
    def getExaCellGlobalCell(self, dbid:int64, begin_snap: int32, end_snap: int32):
        return self.getValue(CdbEnum.EXA_CELL_GLOBAL_CELL, OdbExaCellGlobalCell, 
                            dbid, begin_snap, end_snap)
    
    def getExaCellGlobal(self, dbid:int64, begin_snap: int32, end_snap: int32):
        return self.getValue(CdbEnum.EXA_CELL_GLOBAL, OdbExaCellGlobal, 
                            dbid, begin_snap, end_snap)
         
    def getExaIoReason(self, dbid:int64, begin_snap: int32, end_snap: int32):
        return self.getValue(CdbEnum.EXA_IO_REASON, OdbExaIoReason, 
                            dbid, begin_snap, end_snap)
    
    def getExaCellAlert(self, dbid:int64, begin_snap: int32, end_snap: int32):
        return self.getValue(CdbEnum.EXA_CELL_ALERT, OdbExaCellAlert, 
                            dbid, begin_snap, end_snap)
         
    def getExaAsmDiskgroup(self, dbid:int64, begin_snap: int32, end_snap: int32):
        return self.getValue(CdbEnum.EXA_ASM_DISKGROUP, OdbExaAsmDiskgroup, 
                            dbid, begin_snap, end_snap)
    
    def getAshCpuWaitAnalysicReport(self, dbid:int64, begin_snap: int32, end_snap: int32):
        return self.getValue(CdbEnum.ASH_CPU_WAIT_ANALYSIC_REPORT, CdbAshCpuWaitAnalysicReport, 
                            dbid, begin_snap, end_snap)

    def getAshTopEventBySnap(self, dbid:int64, begin_snap: int32, end_snap: int32):
            return self.getValue(CdbEnum.ASH_TOP_EVENT_BY_SNAP, CdbAshTopEventBySnap, 
                                dbid, begin_snap, end_snap)

    def getAshSqlEventBySnap(self, dbid:int64, begin_snap: int32, end_snap: int32):
            return self.getValue(CdbEnum.ASH_SQL_EVENT_BY_SNAP, CdbAshSqlEventBySnap, 
                                dbid, begin_snap, end_snap)

    def getAshTopSegmentBySnap(self, dbid:int64, begin_snap: int32, end_snap: int32):
            return self.getValue(CdbEnum.ASH_TOP_SEGMENT_BY_SNAP, CdbAshTopSegmentBySnap, 
                                dbid, begin_snap, end_snap)

    def getAshTopSegmentEventBySnap(self, dbid:int64, begin_snap: int32, end_snap: int32):
            return self.getValue(CdbEnum.ASH_TOP_SEGMENT_EVENT_BY_SNAP, CdbAshTopSegmentEventBySnap, 
                                dbid, begin_snap, end_snap)

    def getAshTopSegmentSqlEventBySnap(self, dbid:int64, begin_snap: int32, end_snap: int32):
            return self.getValue(CdbEnum.ASH_TOP_SEGMENT_SQL_EVENT_BY_SNAP, CdbAshTopSegmentSqlEventBySnap, 
                                dbid, begin_snap, end_snap)

    def getAshSqlPlanEventBySnap(self, dbid:int64, begin_snap: int32, end_snap: int32):
            return self.getValue(CdbEnum.ASH_SQL_PLAN_EVENT_BY_SNAP, CdbAshSqlPlanEventBySnap, 
                                dbid, begin_snap, end_snap)

    def getAshTopSqlCostBySnap(self, dbid:int64, begin_snap: int32, end_snap: int32):
            return self.getValue(CdbEnum.ASH_TOP_SQL_COST_BY_SNAP, CdbAshTopSqlCostBySnap, 
                                dbid, begin_snap, end_snap)

    def getAshTopEventBackground(self, dbid:int64, begin_snap: int32, end_snap: int32):
            return self.getValue(CdbEnum.ASH_TOP_EVENT_BACKGROUND, CdbAshTopEventBackground, 
                                dbid, begin_snap, end_snap)

    def getAshTopEventNotBackground(self, dbid:int64, begin_snap: int32, end_snap: int32):
            return self.getValue(CdbEnum.ASH_TOP_EVENT_NOT_BACKGROUND, CdbAshTopEventBackground, 
                                dbid, begin_snap, end_snap)

    '''ASH Event    '''    
    def getAshEventObjForeground(self, dbid:int64, begin_snap: int32, end_snap: int32):
            return self.getValue(CdbEnum.ASH_EVENT_OBJ_FOREGROUND, CdbAshEvent, 
                                dbid, begin_snap, end_snap)

    def getAshEventObjForegroundByDb(self, dbid:int64, begin_snap: int32, end_snap: int32):
            return self.getValue(CdbEnum.ASH_EVENT_OBJ_FOREGROUND_BY_DB, CdbAshEvent, 
                                dbid, begin_snap, end_snap)

    def getAshEventGc(self, dbid:int64, begin_snap: int32, end_snap: int32):
            return self.getValue(CdbEnum.ASH_EVENT_GC, CdbAshEvent, 
                                dbid, begin_snap, end_snap)

    def getAshEventGcByDb(self, dbid:int64, begin_snap: int32, end_snap: int32):
            return self.getValue(CdbEnum.ASH_EVENT_GC_BY_DB, CdbAshEvent, 
                                dbid, begin_snap, end_snap)

    def getAshEventEnq(self, dbid:int64, begin_snap: int32, end_snap: int32):
            return self.getValue(CdbEnum.ASH_EVENT_ENQ, CdbAshEvent, 
                                dbid, begin_snap, end_snap)

    def getAshEventEnqByDb(self, dbid:int64, begin_snap: int32, end_snap: int32):
            return self.getValue(CdbEnum.ASH_EVENT_ENQ_BY_DB, CdbAshEvent, 
                                dbid, begin_snap, end_snap)

    def getAshEventLatch(self, dbid:int64, begin_snap: int32, end_snap: int32):
            return self.getValue(CdbEnum.ASH_EVENT_LATCH, CdbAshEvent, 
                                dbid, begin_snap, end_snap)

    def getAshEventLatchByDb(self, dbid:int64, begin_snap: int32, end_snap: int32):
            return self.getValue(CdbEnum.ASH_EVENT_LATCH_BY_DB, CdbAshEvent, 
                                dbid, begin_snap, end_snap)

    def getAshEventDirect(self, dbid:int64, begin_snap: int32, end_snap: int32):
            return self.getValue(CdbEnum.ASH_EVENT_DIRECT, CdbAshEvent, 
                                dbid, begin_snap, end_snap)

    def getAshEventDirectByDb(self, dbid:int64, begin_snap: int32, end_snap: int32):
            return self.getValue(CdbEnum.ASH_EVENT_DIRECT_BY_DB, CdbAshEvent, 
                                dbid, begin_snap, end_snap)

    def getAshEventDbfile(self, dbid:int64, begin_snap: int32, end_snap: int32):
            return self.getValue(CdbEnum.ASH_EVENT_DBFILE, CdbAshEvent, 
                                dbid, begin_snap, end_snap)

    def getAshEventDbfileByDb(self, dbid:int64, begin_snap: int32, end_snap: int32):
            return self.getValue(CdbEnum.ASH_EVENT_DBFILE_BY_DB, CdbAshEvent, 
                                dbid, begin_snap, end_snap)

    def getAshEventCell(self, dbid:int64, begin_snap: int32, end_snap: int32):
            return self.getValue(CdbEnum.ASH_EVENT_CELL, CdbAshEvent, 
                                dbid, begin_snap, end_snap)

    def getAshEventCellByDb(self, dbid:int64, begin_snap: int32, end_snap: int32):
            return self.getValue(CdbEnum.ASH_EVENT_CELL_BY_DB, CdbAshEvent, 
                                dbid, begin_snap, end_snap)

    def getAshEventRowlock(self, dbid:int64, begin_snap: int32, end_snap: int32):
            return self.getValue(CdbEnum.ASH_EVENT_ROWLOCK, CdbAshEvent, 
                                dbid, begin_snap, end_snap)

    def getAshEventItl(self, dbid:int64, begin_snap: int32, end_snap: int32):
            return self.getValue(CdbEnum.ASH_EVENT_ITL, CdbAshEvent, 
                                dbid, begin_snap, end_snap)

    def getAshEventIndexContention(self, dbid:int64, begin_snap: int32, end_snap: int32):
            return self.getValue(CdbEnum.ASH_EVENT_INDEX_CONTENTION, CdbAshEvent, 
                                dbid, begin_snap, end_snap)

    def getAshEventBufferBusy(self, dbid:int64, begin_snap: int32, end_snap: int32):
            return self.getValue(CdbEnum.ASH_EVENT_BUFFER_BUSY, CdbAshEvent, 
                                dbid, begin_snap, end_snap)

    def getAshEventHwContention(self, dbid:int64, begin_snap: int32, end_snap: int32):
            return self.getValue(CdbEnum.ASH_EVENT_HW_CONTENTION, CdbAshEvent, 
                                dbid, begin_snap, end_snap)
    '''End CdbAshEvent'''
    
    '''ASH SqlId'''
    def getAshSqlIdEvent(self, dbid:int64, begin_snap: int32, end_snap: int32):
            return self.getValue(CdbEnum.ASH_SQL_ID_EVENT, CdbAshSqlId, 
                                dbid, begin_snap, end_snap)

    def getAshSqlIdSqContention(self, dbid:int64, begin_snap: int32, end_snap: int32):
            return self.getValue(CdbEnum.ASH_SQL_ID_SQ_CONTENTION, CdbAshSqlId, 
                                dbid, begin_snap, end_snap)

    def getAshSqlIdCursor(self, dbid:int64, begin_snap: int32, end_snap: int32):
            return self.getValue(CdbEnum.ASH_SQL_ID_CURSOR, CdbAshSqlId, 
                                dbid, begin_snap, end_snap)

    def getAshSqlIdRowcache(self, dbid:int64, begin_snap: int32, end_snap: int32):
            return self.getValue(CdbEnum.ASH_SQL_ID_ROWCACHE, CdbAshSqlId, 
                                dbid, begin_snap, end_snap)

    def getAshSqlIdIoWaits(self, dbid:int64, begin_snap: int32, end_snap: int32):
            return self.getValue(CdbEnum.ASH_SQL_ID_IO_WAITS, CdbAshSqlId, 
                                dbid, begin_snap, end_snap)

    '''End CdbAshSqlId'''

    def getAshSqlPlanChange(self, dbid:int64, begin_snap: int32, end_snap: int32):
            return self.getValue(CdbEnum.SQL_PLAN_CHANGE, CdbAshSqlPlanChange, 
                                dbid, begin_snap, end_snap)

    def getAshWaitClass(self, dbid:int64, begin_snap: int32, end_snap: int32):
            return self.getValue(CdbEnum.ASH_WAIT_CLASS, CdbAshWaitClass, 
                                dbid, begin_snap, end_snap)

    def getDbTopSegmentTableScans(self, dbid:int64, begin_snap: int32, end_snap: int32):
        return self.getValue(CdbEnum.DB_TOP_SEGMENT_TABLE_SCANS, CdbSegmentTableScans, 
                             dbid, begin_snap, end_snap)

    def getDbTopSegmentPhysicalWriteIops(self, dbid:int64, begin_snap: int32, end_snap: int32):
        return self.getValue(CdbEnum.DB_TOP_SEGMENT_PHYSICAL_WRITE_IOPS, CdbSegmentPhysicalWriteIops, 
                            dbid, begin_snap, end_snap)

    def getDbTopSegmentPhysicalWriteDir(self, dbid:int64, begin_snap: int32, end_snap: int32):
        return self.getValue(CdbEnum.DB_TOP_SEGMENT_PHYSICAL_WRITE_DIR, CdbSegmentPhysicalWriteDir, 
                            dbid, begin_snap, end_snap)

    def getDbTopSegmentRowLock(self, dbid:int64, begin_snap: int32, end_snap: int32):
        return self.getValue(CdbEnum.DB_TOP_SEGMENT_ROW_LOCK, CdbSegmentRowLock, 
                            dbid, begin_snap, end_snap)

    def getDbTopSegmentPhysicalWrite(self, dbid:int64, begin_snap: int32, end_snap: int32):
        return self.getValue(CdbEnum.DB_TOP_SEGMENT_PHYSICAL_WRITE, CdbSegmentPhysicalWrite, 
                            dbid, begin_snap, end_snap)

    def getDbTopSegmentPhysicalReadIops(self, dbid:int64, begin_snap: int32, end_snap: int32):
        return self.getValue(CdbEnum.DB_TOP_SEGMENT_PHYSICAL_READ_IOPS, CdbSegmentPhysicalReadIops, 
                            dbid, begin_snap, end_snap)

    def getDbTopSegmentPhysicalReadDir(self, dbid:int64, begin_snap: int32, end_snap: int32):
        return self.getValue(CdbEnum.DB_TOP_SEGMENT_PHYSICAL_READ_DIR, CdbSegmentPhysicalReadDir, 
                            dbid, begin_snap, end_snap)

    def getDbTopSegmentPhysicalRead(self, dbid:int64, begin_snap: int32, end_snap: int32):
        return self.getValue(CdbEnum.DB_TOP_SEGMENT_PHYSICAL_READ, CdbSegmentPhysicalRead, 
                            dbid, begin_snap, end_snap)

    def getDbTopSegmentOptPhysicalRead(self, dbid:int64, begin_snap: int32, end_snap: int32):
        return self.getValue(CdbEnum.DB_TOP_SEGMENT_OPT_PHYSICAL_READ, CdbSegmentOptPhysicalRead, 
                            dbid, begin_snap, end_snap)

    def getDbTopSegmentLogicalRead(self, dbid:int64, begin_snap: int32, end_snap: int32):
        return self.getValue(CdbEnum.DB_TOP_SEGMENT_LOGICAL_READ, CdbSegmentLogicalRead, 
                            dbid, begin_snap, end_snap)

    def getDbTopSegmentItlWaits(self, dbid:int64, begin_snap: int32, end_snap: int32):
        return self.getValue(CdbEnum.DB_TOP_SEGMENT_ITL_WAITS, CdbSegmentItlWaits, 
                            dbid, begin_snap, end_snap)

    def getDbTopSegmentGcCurrentBlockSrv(self, dbid:int64, begin_snap: int32, end_snap: int32):
        return self.getValue(CdbEnum.DB_TOP_SEGMENT_GC_CURRENT_BLOCK_SRV, CdbSegmentGcCurrentBlockSrv, 
                            dbid, begin_snap, end_snap)

    def getDbTopSegmentGcCurrentBlockRec(self, dbid:int64, begin_snap: int32, end_snap: int32):
        return self.getValue(CdbEnum.DB_TOP_SEGMENT_GC_CURRENT_BLOCK_REC, CdbSegmentGcCurrentBlockRec, 
                            dbid, begin_snap, end_snap)

    def getDbTopSegmentGcCrBlockSrv(self, dbid:int64, begin_snap: int32, end_snap: int32):
        return self.getValue(CdbEnum.DB_TOP_SEGMENT_GC_CR_BLOCK_SRV, CdbSegmentGcCrBlockSrv, 
                            dbid, begin_snap, end_snap)

    def getDbTopSegmentGcCrBlockRec(self, dbid:int64, begin_snap: int32, end_snap: int32):
        return self.getValue(CdbEnum.DB_TOP_SEGMENT_GC_CR_BLOCK_REC, CdbSegmentGcCrBlockRec, 
                            dbid, begin_snap, end_snap)

    def getDbTopSegmentGcBufferBusyWait(self, dbid:int64, begin_snap: int32, end_snap: int32):
        return self.getValue(CdbEnum.DB_TOP_SEGMENT_GC_BUFFER_BUSY_WAIT, CdbSegmentGcBufferBusyWait, 
                            dbid, begin_snap, end_snap)

    def getDbTopSegmentChainRow(self, dbid:int64, begin_snap: int32, end_snap: int32):
        return self.getValue(CdbEnum.DB_TOP_SEGMENT_CHAIN_ROW, CdbSegmentChainRow, 
                            dbid, begin_snap, end_snap)

    def getDbTopSegmentBufferBusyWait(self, dbid:int64, begin_snap: int32, end_snap: int32):
        return self.getValue(CdbEnum.DB_TOP_SEGMENT_BUFFER_BUSY_WAIT, CdbSegmentBufferBusyWait, 
                            dbid, begin_snap, end_snap)

    def getDbTopSegmentBlockChange(self, dbid:int64, begin_snap: int32, end_snap: int32):
        return self.getValue(CdbEnum.DB_TOP_SEGMENT_BLOCK_CHANGE, CdbSegmentBlockChange, 
                            dbid, begin_snap, end_snap)

    '''Segment Snapshot'''
    def getDbTopSegmentSnapTableScans(self, dbid:int64, begin_snap: int32, end_snap: int32):
        return self.getValue(CdbEnum.DB_TOP_SEGMENT_SNAP_TABLE_SCANS, CdbSegmentSnaps, 
                            dbid, begin_snap, end_snap)

    def getDbTopSegmentSnapPhysicalWriteIops(self, dbid:int64, begin_snap: int32, end_snap: int32):
        return self.getValue(CdbEnum.DB_TOP_SEGMENT_SNAP_PHYSICAL_WRITE_IOPS, CdbSegmentSnaps, 
                            dbid, begin_snap, end_snap)

    def getDbTopSegmentSnapPhysicalWriteDir(self, dbid:int64, begin_snap: int32, end_snap: int32):
        return self.getValue(CdbEnum.DB_TOP_SEGMENT_SNAP_PHYSICAL_WRITE_DIR, CdbSegmentSnaps, 
                            dbid, begin_snap, end_snap)

    def getDbTopSegmentSnapRowLock(self, dbid:int64, begin_snap: int32, end_snap: int32):
        return self.getValue(CdbEnum.DB_TOP_SEGMENT_SNAP_ROW_LOCK, CdbSegmentSnaps, 
                            dbid, begin_snap, end_snap)

    def getDbTopSegmentSnapPhysicalWrite(self, dbid:int64, begin_snap: int32, end_snap: int32):
        return self.getValue(CdbEnum.DB_TOP_SEGMENT_SNAP_PHYSICAL_WRITE, CdbSegmentSnaps, 
                            dbid, begin_snap, end_snap)

    def getDbTopSegmentSnapPhysicalReadIops(self, dbid:int64, begin_snap: int32, end_snap: int32):
        return self.getValue(CdbEnum.DB_TOP_SEGMENT_SNAP_PHYSICAL_READ_IOPS, CdbSegmentSnaps, 
                            dbid, begin_snap, end_snap)

    def getDbTopSegmentSnapPhysicalReadDir(self, dbid:int64, begin_snap: int32, end_snap: int32):
        return self.getValue(CdbEnum.DB_TOP_SEGMENT_SNAP_PHYSICAL_READ_DIR, CdbSegmentSnaps, 
                            dbid, begin_snap, end_snap)

    def getDbTopSegmentSnapPhysicalRead(self, dbid:int64, begin_snap: int32, end_snap: int32):
        return self.getValue(CdbEnum.DB_TOP_SEGMENT_SNAP_PHYSICAL_READ, CdbSegmentSnaps, 
                            dbid, begin_snap, end_snap)

    def getDbTopSegmentSnapOptPhysicalRead(self, dbid:int64, begin_snap: int32, end_snap: int32):
        return self.getValue(CdbEnum.DB_TOP_SEGMENT_SNAP_OPT_PHYSICAL_READ, CdbSegmentSnaps, 
                            dbid, begin_snap, end_snap)

    def getDbTopSegmentSnapLogicalRead(self, dbid:int64, begin_snap: int32, end_snap: int32):
        return self.getValue(CdbEnum.DB_TOP_SEGMENT_SNAP_LOGICAL_READ, CdbSegmentSnaps, 
                            dbid, begin_snap, end_snap)

    def getDbTopSegmentSnapItlWaits(self, dbid:int64, begin_snap: int32, end_snap: int32):
        return self.getValue(CdbEnum.DB_TOP_SEGMENT_SNAP_ITL_WAITS, CdbSegmentSnaps, 
                            dbid, begin_snap, end_snap)

    def getDbTopSegmentSnapGcCurrentBlockSrv(self, dbid:int64, begin_snap: int32, end_snap: int32):
        return self.getValue(CdbEnum.DB_TOP_SEGMENT_SNAP_GC_CURRENT_BLOCK_SRV, CdbSegmentSnaps, 
                            dbid, begin_snap, end_snap)

    def getDbTopSegmentSnapGcCurrentBlockRec(self, dbid:int64, begin_snap: int32, end_snap: int32):
        return self.getValue(CdbEnum.DB_TOP_SEGMENT_SNAP_GC_CURRENT_BLOCK_REC, CdbSegmentSnaps, 
                            dbid, begin_snap, end_snap)

    def getDbTopSegmentSnapGcCrBlockSrv(self, dbid:int64, begin_snap: int32, end_snap: int32):
        return self.getValue(CdbEnum.DB_TOP_SEGMENT_SNAP_GC_CR_BLOCK_SRV, CdbSegmentSnaps, 
                            dbid, begin_snap, end_snap)

    def getDbTopSegmentSnapGcCrBlockRec(self, dbid:int64, begin_snap: int32, end_snap: int32):
        return self.getValue(CdbEnum.DB_TOP_SEGMENT_SNAP_GC_CR_BLOCK_REC, CdbSegmentSnaps, 
                            dbid, begin_snap, end_snap)

    def getDbTopSegmentSnapGcBufferBusyWait(self, dbid:int64, begin_snap: int32, end_snap: int32):
        return self.getValue(CdbEnum.DB_TOP_SEGMENT_SNAP_GC_BUFFER_BUSY_WAIT, CdbSegmentSnaps, 
                            dbid, begin_snap, end_snap)

    def getDbTopSegmentSnapChainRow(self, dbid:int64, begin_snap: int32, end_snap: int32):
        return self.getValue(CdbEnum.DB_TOP_SEGMENT_SNAP_CHAIN_ROW, CdbSegmentSnaps, 
                            dbid, begin_snap, end_snap)

    def getDbTopSegmentSnapBufferBusyWait(self, dbid:int64, begin_snap: int32, end_snap: int32):
        return self.getValue(CdbEnum.DB_TOP_SEGMENT_SNAP_BUFFER_BUSY_WAIT, CdbSegmentSnaps, 
                            dbid, begin_snap, end_snap)

    def getDbTopSegmentSnapBlockChange(self, dbid:int64, begin_snap: int32, end_snap: int32):
        return self.getValue(CdbEnum.DB_TOP_SEGMENT_SNAP_BLOCK_CHANGE, CdbSegmentSnaps, 
                            dbid, begin_snap, end_snap)
    '''End SegmentSnaps'''

    def getDbTopSqlTotalExec(self, dbid:int64, begin_snap: int32, end_snap: int32):
        return self.getValue(CdbEnum.DB_TOP_SQL_TOTAL_EXEC, CdbSqlTotalExec, 
                            dbid, begin_snap, end_snap)

    def getDbTopSqlVersions(self, dbid:int64, begin_snap: int32, end_snap: int32):
        return self.getValue(CdbEnum.DB_TOP_SQL_VERSIONS, CdbSqlVersions, 
                            dbid, begin_snap, end_snap)

    def getDbTopSqlOffLoadReturn(self, dbid:int64, begin_snap: int32, end_snap: int32):
        return self.getValue(CdbEnum.DB_TOP_SQL_OFF_LOAD_RETURN, CdbSqlOffLoadReturn, 
                            dbid, begin_snap, end_snap)

    def getDbTopSqlOffLoad(self, dbid:int64, begin_snap: int32, end_snap: int32):
        return self.getValue(CdbEnum.DB_TOP_SQL_OFF_LOAD, CdbSqlOffLoad, 
                            dbid, begin_snap, end_snap)

    def getDbTopSqlPhysicalWriteMb(self, dbid:int64, begin_snap: int32, end_snap: int32):
        return self.getValue(CdbEnum.DB_TOP_SQL_PHYSICAL_WRITE_MB, CdbSqlPhysicalWriteMb, 
                            dbid, begin_snap, end_snap)

    def getDbTopSqlPhysicalReadMb(self, dbid:int64, begin_snap: int32, end_snap: int32):
        return self.getValue(CdbEnum.DB_TOP_SQL_PHYSICAL_READ_MB, CdbSqlPhysicalReadMb, 
                            dbid, begin_snap, end_snap)

    def getDbTopSqlParseCall(self, dbid:int64, begin_snap: int32, end_snap: int32):
        return self.getValue(CdbEnum.DB_TOP_SQL_PARSE_CALL, CdbSqlParseCall, 
                            dbid, begin_snap, end_snap)

    def getDbTopSqlCpu(self, dbid:int64, begin_snap: int32, end_snap: int32):
        return self.getValue(CdbEnum.DB_TOP_SQL_CPU, CdbSqlCpu, 
                            dbid, begin_snap, end_snap)

    def getDbTopSqlIoWait(self, dbid:int64, begin_snap: int32, end_snap: int32):
        return self.getValue(CdbEnum.DB_TOP_SQL_IO_WAIT, CdbSqlIoWait, 
                            dbid, begin_snap, end_snap)

    def getDbTopSqlCwait(self, dbid:int64, begin_snap: int32, end_snap: int32):
        return self.getValue(CdbEnum.DB_TOP_SQL_CWAIT, CdbSqlCwait, 
                            dbid, begin_snap, end_snap)

    def getDbTopSqlCcWait(self, dbid:int64, begin_snap: int32, end_snap: int32):
        return self.getValue(CdbEnum.DB_TOP_SQL_CC_WAIT, CdbSqlCcWait, 
                            dbid, begin_snap, end_snap)

    def getDbTopSqlAppWait(self, dbid:int64, begin_snap: int32, end_snap: int32):
        return self.getValue(CdbEnum.DB_TOP_SQL_APP_WAIT, CdbSqlAppWait, 
                            dbid, begin_snap, end_snap)

    def getDbTopSqlElapsed(self, dbid:int64, begin_snap: int32, end_snap: int32):
        return self.getValue(CdbEnum.DB_TOP_SQL_ELAPSED, CdbSqlElapsed, 
                            dbid, begin_snap, end_snap)

    def getDbTopSqlLogicalRead(self, dbid:int64, begin_snap: int32, end_snap: int32):
        return self.getValue(CdbEnum.DB_TOP_SQL_LOGICAL_READ, CdbSqlLogicalRead, 
                            dbid, begin_snap, end_snap)

    def getDbTopSqlDiskReads(self, dbid:int64, begin_snap: int32, end_snap: int32):
        return self.getValue(CdbEnum.DB_TOP_SQL_DISK_READS, CdbSqlDiskReads, 
                            dbid, begin_snap, end_snap)

    def getDbTopSqlPhysicalReadIops(self, dbid:int64, begin_snap: int32, end_snap: int32):
        return self.getValue(CdbEnum.DB_TOP_SQL_PHYSICAL_READ_IOPS, CdbSqlPhysicalReadIops, 
                            dbid, begin_snap, end_snap)

    def getDbTopSqlPhysicalWriteIops(self, dbid:int64, begin_snap: int32, end_snap: int32):
        return self.getValue(CdbEnum.DB_TOP_SQL_PHYSICAL_WRITE_IOPS, CdbSqlPhysicalWriteIops, 
                            dbid, begin_snap, end_snap)

    def getDbTopSqlPhysicalWriteDirIops(self, dbid:int64, begin_snap: int32, end_snap: int32):
        return self.getValue(CdbEnum.DB_TOP_SQL_PHYSICAL_WRITE_DIR_IOPS, CdbSqlPhysicalWriteDirIops, 
                            dbid, begin_snap, end_snap)

    def getDbTopSqlSnapTotalExec(self, dbid:int64, begin_snap: int32, end_snap: int32):
        return self.getValue(CdbEnum.DB_TOP_SQL_SNAP_TOTAL_EXEC, CdbSqlSnapTotalExec, 
                            dbid, begin_snap, end_snap)

    def getDbTopSqlSnapVersions(self, dbid:int64, begin_snap: int32, end_snap: int32):
        return self.getValue(CdbEnum.DB_TOP_SQL_SNAP_VERSIONS, CdbSqlSnapVersions, 
                            dbid, begin_snap, end_snap)

    def getDbTopSqlSnapOffLoadReturn(self, dbid:int64, begin_snap: int32, end_snap: int32):
        return self.getValue(CdbEnum.DB_TOP_SQL_SNAP_OFF_LOAD_RETURN, CdbSqlSnapOffLoadReturn, 
                            dbid, begin_snap, end_snap)

    def getDbTopSqlSnapOffLoad(self, dbid:int64, begin_snap: int32, end_snap: int32):
        return self.getValue(CdbEnum.DB_TOP_SQL_SNAP_OFF_LOAD, CdbSqlSnapOffLoad, 
                            dbid, begin_snap, end_snap)

    def getDbTopSqlSnapPhysicalWriteMb(self, dbid:int64, begin_snap: int32, end_snap: int32):
        return self.getValue(CdbEnum.DB_TOP_SQL_SNAP_PHYSICAL_WRITE_MB, CdbSqlSnapPhysicalWriteMb, 
                            dbid, begin_snap, end_snap)

    def getDbTopSqlSnapPhysicalReadMb(self, dbid:int64, begin_snap: int32, end_snap: int32):
        return self.getValue(CdbEnum.DB_TOP_SQL_SNAP_PHYSICAL_READ_MB, CdbSqlSnapPhysicalReadMb, 
                            dbid, begin_snap, end_snap)

    def getDbTopSqlSnapParseCall(self, dbid:int64, begin_snap: int32, end_snap: int32):
        return self.getValue(CdbEnum.DB_TOP_SQL_SNAP_PARSE_CALL, CdbSqlSnapParseCall, 
                            dbid, begin_snap, end_snap)

    def getDbTopSqlSnapCpu(self, dbid:int64, begin_snap: int32, end_snap: int32):
        return self.getValue(CdbEnum.DB_TOP_SQL_SNAP_CPU, CdbSqlSnapCpu, 
                            dbid, begin_snap, end_snap)

    def getDbTopSqlSnapIowait(self, dbid:int64, begin_snap: int32, end_snap: int32):
        return self.getValue(CdbEnum.DB_TOP_SQL_SNAP_IOWAIT, CdbSqlSnapIoWait, 
                            dbid, begin_snap, end_snap)

    def getDbTopSqlSnapCwait(self, dbid:int64, begin_snap: int32, end_snap: int32):
        return self.getValue(CdbEnum.DB_TOP_SQL_SNAP_CWAIT, CdbSqlSnapCwait, 
                            dbid, begin_snap, end_snap)

    def getDbTopSqlSnapCcWait(self, dbid:int64, begin_snap: int32, end_snap: int32):
        return self.getValue(CdbEnum.DB_TOP_SQL_SNAP_CC_WAIT, CdbSqlSnapCcWait, 
                            dbid, begin_snap, end_snap)

    def getDbTopSqlSnapAppWait(self, dbid:int64, begin_snap: int32, end_snap: int32):
        return self.getValue(CdbEnum.DB_TOP_SQL_SNAP_APP_WAIT, CdbSqlSnapAppWait, 
                            dbid, begin_snap, end_snap)

    def getDbTopSqlSnapElapsed(self, dbid:int64, begin_snap: int32, end_snap: int32):
        return self.getValue(CdbEnum.DB_TOP_SQL_SNAP_ELAPSED, CdbSqlSnapElapsed, 
                            dbid, begin_snap, end_snap)

    def getDbTopSqlSnapLogicalRead(self, dbid:int64, begin_snap: int32, end_snap: int32):
        return self.getValue(CdbEnum.DB_TOP_SQL_SNAP_LOGICAL_READ, CdbSqlSnapLogicalRead, 
                            dbid, begin_snap, end_snap)

    def getDbTopSqlSnapDiskReads(self, dbid:int64, begin_snap: int32, end_snap: int32):
        return self.getValue(CdbEnum.DB_TOP_SQL_SNAP_DISK_READS, CdbSqlSnapDiskReads, 
                            dbid, begin_snap, end_snap)

    def getDbTopSqlSnapPhysicalReadIops(self, dbid:int64, begin_snap: int32, end_snap: int32):
        return self.getValue(CdbEnum.DB_TOP_SQL_SNAP_PHYSICAL_READ_IOPS, CdbSqlSnapPhysicalReadIops, 
                            dbid, begin_snap, end_snap)

    def getDbTopSqlSnapPhysicalWriteIops(self, dbid:int64, begin_snap: int32, end_snap: int32):
        return self.getValue(CdbEnum.DB_TOP_SQL_SNAP_PHYSICAL_WRITE_IOPS, CdbSqlSnapPhysicalWriteIops, 
                            dbid, begin_snap, end_snap)

    def getDbTopSqlSnapPhysicalWriteDirIops(self, dbid:int64, begin_snap: int32, end_snap: int32):
        return self.getValue(CdbEnum.DB_TOP_SQL_SNAP_PHYSICAL_WRITE_DIR_IOPS, CdbSqlSnapPhysicalWriteDirIops, 
                            dbid, begin_snap, end_snap)

    def getDbTopSqlSnapInvalid(self, dbid:int64, begin_snap: int32, end_snap: int32):
        return self.getValue(CdbEnum.DB_TOP_SQL_SNAP_INVALID, CdbSqlSnapInvalid, 
                            dbid, begin_snap, end_snap)
    
    
        # return self.getValue(CdbEnum.DBINFO, DbInfo, 
        #                     dbid, begin_snap, end_snap)
    
    #  = 'cdb.best_practice_19c'
    # def getSqlPlanChange(self, dbid:int64, begin_snap: int32, end_snap: int32):
    #     return self.getValue(CdbEnum.BEST_PRACTICE_19C, AshOverallWaitGlobal, 
    #                         dbid, begin_snap, end_snap)

    def getDbInfo(self, dbid:int64):
         return super().getDbInfo(CdbEnum.DB_INFO.value, dbid)
            
    def getExtractTopSqlCpu(self, top_n_rows:int = 10):
        return self.extractTopSql(CdbEnum.EXTRACT_TOP_SQL_CPU, top_n_rows)

    def getExtractTopSqlWait(self, top_n_rows:int = 10):
        return self.extractTopSql(CdbEnum.EXTRACT_TOP_SQL_WAIT, top_n_rows)

    def getExtractTopSqlIo(self, top_n_rows:int = 10):
        return self.extractTopSql(CdbEnum.EXTRACT_TOP_SQL_IO, top_n_rows)
