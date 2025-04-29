from numpy import int32, int64
from data.db_context import DbContext, DataOperators
from app.data.repositories.general_repository import GeneralRepository
from app.data.entities.non_cdb_models import *
from logger import AppLogger
from app.data.repositories.enum.non_cdb_enum import NonCdbEnum

class NonCdbRepository(GeneralRepository):
    
    _logger = AppLogger().get_logger()
    
    def __init__(self, db_context: DbContext):
        
        if not isinstance(db_context, DataOperators):
            self._logger.error(TypeError("db_context must implement DataOperations"))
        
        self.db_context = db_context
    
    def getDbInfo(self, dbid:int64):
        return super().getDbInfo(NonCdbEnum.DB_INFO.value, dbid)
    
    def getAshOverallWaitClass(self, dbid:int64, begin_snap: int32, end_snap: int32):
        return self.getValue(NonCdbEnum.ASH_OVERALL_WAIT_CLASS, OdbAshOverallWaitClass, 
                             dbid, begin_snap, end_snap)

    def getAshOverallEvent(self, dbid:int64, begin_snap: int32, end_snap: int32):
            return self.getValue(NonCdbEnum.ASH_OVERALL_EVENT, NonCdbAshOverallEvent, 
                                dbid, begin_snap, end_snap)

    def getAshOverallModule(self, dbid:int64, begin_snap: int32, end_snap: int32):
            return self.getValue(NonCdbEnum.ASH_OVERALL_MODULE, OdbAshOverallModule, 
                                dbid, begin_snap, end_snap)

    def getAshOverallProgram(self, dbid:int64, begin_snap: int32, end_snap: int32):
            return self.getValue(NonCdbEnum.ASH_OVERALL_PROGRAM, OdbAshOverallProgram, 
                                dbid, begin_snap, end_snap)

    def getAshOverallSegment(self, dbid:int64, begin_snap: int32, end_snap: int32):
            return self.getValue(NonCdbEnum.ASH_OVERALL_SEGMENT, NonCdbAshOverallSegment, 
                                dbid, begin_snap, end_snap)

    def getAshOverallIndex(self, dbid:int64, begin_snap: int32, end_snap: int32):
            return self.getValue(NonCdbEnum.ASH_OVERALL_INDEX, NonCdbAshOverallIndex, 
                                dbid, begin_snap, end_snap)

    def getAshOverallTable(self, dbid:int64, begin_snap: int32, end_snap: int32):
            return self.getValue(NonCdbEnum.ASH_OVERALL_TABLE, NonCdbAshOverallTable, 
                                dbid, begin_snap, end_snap)

    def getAshOverallSqlWait(self, dbid:int64, begin_snap: int32, end_snap: int32):
            return self.getValue(NonCdbEnum.ASH_OVERALL_SQL_WAIT, NonCdbAshOverallSqlWait, 
                                dbid, begin_snap, end_snap)

    def getAshOverallSqlCpu(self, dbid:int64, begin_snap: int32, end_snap: int32):
            return self.getValue(NonCdbEnum.ASH_OVERALL_SQL_CPU, NonCdbAshOverallSqlCpu, 
                                dbid, begin_snap, end_snap)

    def getAshOverallSqlIo(self, dbid:int64, begin_snap: int32, end_snap: int32):
            return self.getValue(NonCdbEnum.ASH_OVERALL_SQL_IO, NonCdbAshOverallSqlIo, 
                                dbid, begin_snap, end_snap)

    def getAshOverallOperation(self, dbid:int64, begin_snap: int32, end_snap: int32):
            return self.getValue(NonCdbEnum.ASH_OVERALL_OPERATION, NonCdbAshOverallOperation, 
                                dbid, begin_snap, end_snap)

    def getAshOverallSqlEvent(self, dbid:int64, begin_snap: int32, end_snap: int32):
            return self.getValue(NonCdbEnum.ASH_OVERALL_SQL_EVENT, NonCdbAshOverallSqlEvent, 
                                dbid, begin_snap, end_snap)

    def getAshCpuWaitAnalysicReport(self, dbid:int64, begin_snap: int32, end_snap: int32):
            return self.getValue(NonCdbEnum.ASH_CPU_WAIT_ANALYSIC_REPORT, OdbAshCpuWaitAnalysicReport, 
                                dbid, begin_snap, end_snap)

    def getAshTopEventBySnap(self, dbid:int64, begin_snap: int32, end_snap: int32):
            return self.getValue(NonCdbEnum.ASH_TOP_EVENT_BY_SNAP, OdbAshTopEventBySnap, 
                                dbid, begin_snap, end_snap)

    def getAshSqlEventBySnap(self, dbid:int64, begin_snap: int32, end_snap: int32):
            return self.getValue(NonCdbEnum.ASH_SQL_EVENT_BY_SNAP, OdbAshSqlEventBySnap, 
                                dbid, begin_snap, end_snap)

    def getAshTopSegmentBySnap(self, dbid:int64, begin_snap: int32, end_snap: int32):
            return self.getValue(NonCdbEnum.ASH_TOP_SEGMENT_BY_SNAP, OdbAshTopSegmentBySnap, 
                                dbid, begin_snap, end_snap)

    def getAshTopSegmentEventBySnap(self, dbid:int64, begin_snap: int32, end_snap: int32):
            return self.getValue(NonCdbEnum.ASH_TOP_SEGMENT_EVENT_BY_SNAP, NonCdbAshTopSegmentEventBySnap, 
                                dbid, begin_snap, end_snap)

    def getAshTopSegmentSqlEventBySnap(self, dbid:int64, begin_snap: int32, end_snap: int32):
            return self.getValue(NonCdbEnum.ASH_TOP_SEGMENT_SQL_EVENT_BY_SNAP, OdbAshTopSegmentSqlEventBySnap, 
                                dbid, begin_snap, end_snap)

    def getAshSqlPlanEventBySnap(self, dbid:int64, begin_snap: int32, end_snap: int32):
            return self.getValue(NonCdbEnum.ASH_SQL_PLAN_EVENT_BY_SNAP, OdbAshSqlPlanEventBySnap, 
                                dbid, begin_snap, end_snap)

    def getAshTopSqlCostBySnap(self, dbid:int64, begin_snap: int32, end_snap: int32):
            return self.getValue(NonCdbEnum.ASH_TOP_SQL_COST_BY_SNAP, OdbAshTopSqlCostBySnap, 
                                dbid, begin_snap, end_snap)

    def getAshTopEventBackground(self, dbid:int64, begin_snap: int32, end_snap: int32):
            return self.getValue(NonCdbEnum.ASH_TOP_EVENT_BACKGROUND, OdbAshTopEventBackground, 
                                dbid, begin_snap, end_snap)

    '''ASH EVENT'''
    def getAshEventObjForeground(self, dbid:int64, begin_snap: int32, end_snap: int32):
            return self.getValue(NonCdbEnum.ASH_EVENT_OBJ_FOREGROUND, OdbAshEvent, 
                                dbid, begin_snap, end_snap)

    def getAshEventObjForegroundByDb(self, dbid:int64, begin_snap: int32, end_snap: int32):
            return self.getValue(NonCdbEnum.ASH_EVENT_OBJ_FOREGROUND_BY_DB, OdbAshEvent, 
                                dbid, begin_snap, end_snap)

    def getAshEventGc(self, dbid:int64, begin_snap: int32, end_snap: int32):
            return self.getValue(NonCdbEnum.ASH_EVENT_GC, OdbAshEvent, 
                                dbid, begin_snap, end_snap)

    def getAshEventGcByDb(self, dbid:int64, begin_snap: int32, end_snap: int32):
            return self.getValue(NonCdbEnum.ASH_EVENT_GC_BY_DB, OdbAshEvent, 
                                dbid, begin_snap, end_snap)

    def getAshEventEnq(self, dbid:int64, begin_snap: int32, end_snap: int32):
            return self.getValue(NonCdbEnum.ASH_EVENT_ENQ, OdbAshEvent, 
                                dbid, begin_snap, end_snap)

    def getAshEventEnqByDb(self, dbid:int64, begin_snap: int32, end_snap: int32):
            return self.getValue(NonCdbEnum.ASH_EVENT_ENQ_BY_DB, OdbAshEvent, 
                                dbid, begin_snap, end_snap)

    def getAshEventLatch(self, dbid:int64, begin_snap: int32, end_snap: int32):
            return self.getValue(NonCdbEnum.ASH_EVENT_LATCH, OdbAshEvent, 
                                dbid, begin_snap, end_snap)

    def getAshEventLatchByDb(self, dbid:int64, begin_snap: int32, end_snap: int32):
            return self.getValue(NonCdbEnum.ASH_EVENT_LATCH_BY_DB, OdbAshEvent, 
                                dbid, begin_snap, end_snap)

    def getAshEventDirect(self, dbid:int64, begin_snap: int32, end_snap: int32):
            return self.getValue(NonCdbEnum.ASH_EVENT_DIRECT, OdbAshEvent, 
                                dbid, begin_snap, end_snap)

    def getAshEventDirectByDb(self, dbid:int64, begin_snap: int32, end_snap: int32):
            return self.getValue(NonCdbEnum.ASH_EVENT_DIRECT_BY_DB, OdbAshEvent, 
                                dbid, begin_snap, end_snap)

    def getAshEventDbfile(self, dbid:int64, begin_snap: int32, end_snap: int32):
            return self.getValue(NonCdbEnum.ASH_EVENT_DBFILE, OdbAshEvent, 
                                dbid, begin_snap, end_snap)

    def getAshEventDbfileByDb(self, dbid:int64, begin_snap: int32, end_snap: int32):
            return self.getValue(NonCdbEnum.ASH_EVENT_DBFILE_BY_DB, OdbAshEvent, 
                                dbid, begin_snap, end_snap)

    def getAshEventCell(self, dbid:int64, begin_snap: int32, end_snap: int32):
            return self.getValue(NonCdbEnum.ASH_EVENT_CELL, OdbAshEvent, 
                                dbid, begin_snap, end_snap)

    def getAshEventCellByDb(self, dbid:int64, begin_snap: int32, end_snap: int32):
            return self.getValue(NonCdbEnum.ASH_EVENT_CELL_BY_DB, OdbAshEvent, 
                                dbid, begin_snap, end_snap)

    def getAshEventRowLock(self, dbid:int64, begin_snap: int32, end_snap: int32):
            return self.getValue(NonCdbEnum.ASH_EVENT_ROW_LOCK, OdbAshEvent, 
                                dbid, begin_snap, end_snap)

    def getAshEventItl(self, dbid:int64, begin_snap: int32, end_snap: int32):
            return self.getValue(NonCdbEnum.ASH_EVENT_ITL, OdbAshEvent, 
                                dbid, begin_snap, end_snap)

    def getAshEventIndexContention(self, dbid:int64, begin_snap: int32, end_snap: int32):
            return self.getValue(NonCdbEnum.ASH_EVENT_INDEX_CONTENTION, OdbAshEvent, 
                                dbid, begin_snap, end_snap)

    def getAshEventBufferBusy(self, dbid:int64, begin_snap: int32, end_snap: int32):
            return self.getValue(NonCdbEnum.ASH_EVENT_BUFFER_BUSY, OdbAshEvent, 
                                dbid, begin_snap, end_snap)

    def getAshEventHwContention(self, dbid:int64, begin_snap: int32, end_snap: int32):
            return self.getValue(NonCdbEnum.ASH_EVENT_HW_CONTENTION, OdbAshEvent, 
                                dbid, begin_snap, end_snap)
    '''END ASH EVENT'''
    
    '''ASH SQL_ID'''
    def getAshSqlIdEvent(self, dbid:int64, begin_snap: int32, end_snap: int32):
            return self.getValue(NonCdbEnum.ASH_SQL_ID_EVENT, NonCdbAshSqlId, 
                                dbid, begin_snap, end_snap)

    def getAshSqlIdSqContention(self, dbid:int64, begin_snap: int32, end_snap: int32):
            return self.getValue(NonCdbEnum.ASH_SQL_ID_SQ_CONTENTION, NonCdbAshSqlIdSqContention, 
                                dbid, begin_snap, end_snap)

    def getAshSqlIdCursor(self, dbid:int64, begin_snap: int32, end_snap: int32):
            return self.getValue(NonCdbEnum.ASH_SQL_ID_CURSOR, NonCdbAshSqlId, 
                                dbid, begin_snap, end_snap)

    def getAshSqlIdRowCache(self, dbid:int64, begin_snap: int32, end_snap: int32):
            return self.getValue(NonCdbEnum.ASH_SQL_ID_ROW_CACHE, NonCdbAshSqlId, 
                                dbid, begin_snap, end_snap)

    def getAshSqlIdIoWaits(self, dbid:int64, begin_snap: int32, end_snap: int32):
            return self.getValue(NonCdbEnum.ASH_SQL_ID_IO_WAITS, NonCdbAshSqlId, 
                                dbid, begin_snap, end_snap)
    '''END ASH SQL_ID'''

    def getAshSqlPlanChange(self, dbid:int64, begin_snap: int32, end_snap: int32):
            return self.getValue(NonCdbEnum.ASH_SQL_PLAN_CHANGE, OdbAshSqlPlanChange, 
                                dbid, begin_snap, end_snap)

    def getAshWaitClass(self, dbid:int64, begin_snap: int32, end_snap: int32):
            return self.getValue(NonCdbEnum.ASH_WAIT_CLASS, OdbAshWaitClass, 
                                dbid, begin_snap, end_snap)

    def getDbaHistoryStatistic(self, dbid:int64, begin_snap: int32, end_snap: int32):
            return self.getValue(NonCdbEnum.DBA_HISTORY_STATISTIC, NonCdbDbaHistoryStatistic, 
                                dbid, begin_snap, end_snap)

    def getDbWeAas(self, dbid:int64, begin_snap: int32, end_snap: int32):
            return self.getValue(NonCdbEnum.DB_WE_AAS, OdbDbWeAas, 
                                dbid, begin_snap, end_snap)

    def getIoFileTypeStatistic(self, dbid:int64, begin_snap: int32, end_snap: int32):
            return self.getValue(NonCdbEnum.IO_FILE_TYPE_STATISTIC, NonCdbIoFileTypeStatistic, 
                                dbid, begin_snap, end_snap)

    def getIoFileTypeStatisticGlobal(self, dbid:int64, begin_snap: int32, end_snap: int32):
            return self.getValue(NonCdbEnum.IO_FILE_TYPE_STATISTIC_GLOBAL, NonCdbIoFileTypeStatisticGlobal, 
                                dbid, begin_snap, end_snap)

    def getLatchStatistic(self, dbid:int64, begin_snap: int32, end_snap: int32):
            return self.getValue(NonCdbEnum.LATCH_STATISTIC, OdbLatchStatistic, 
                                dbid, begin_snap, end_snap)

    def getLibraryCacheStatistic(self, dbid:int64, begin_snap: int32, end_snap: int32):
            return self.getValue(NonCdbEnum.LIBRARY_CACHE_STATISTIC, OdbLibraryCacheStatistic, 
                                dbid, begin_snap, end_snap)

    def getOsStatistic(self, dbid:int64, begin_snap: int32, end_snap: int32):
            return self.getValue(NonCdbEnum.OS_STATISTIC, OdbOsStatistic, 
                                dbid, begin_snap, end_snap)

    def getPgaStatistic(self, dbid:int64, begin_snap: int32, end_snap: int32):
            return self.getValue(NonCdbEnum.PGA_STATISTIC, OdbPgaStatistic, 
                                dbid, begin_snap, end_snap)

    def getDbWcAas(self, dbid:int64, begin_snap: int32, end_snap: int32):
            return self.getValue(NonCdbEnum.DB_WC_AAS, OdbDbWcAas, 
                                dbid, begin_snap, end_snap)

    def getDbTopSqlSnapIoWait(self, dbid:int64, begin_snap: int32, end_snap: int32):
            return self.getValue(NonCdbEnum.DB_TOP_SQL_SNAP_IO_WAIT, NonCdbSqlSnapIoWait, 
                                dbid, begin_snap, end_snap)

    def getDbTopSqlSnapCwait(self, dbid:int64, begin_snap: int32, end_snap: int32):
            return self.getValue(NonCdbEnum.DB_TOP_SQL_SNAP_CWAIT, NonCdbSqlSnapCwait, 
                                dbid, begin_snap, end_snap)

    def getDbTopSqlSnapElapsed(self, dbid:int64, begin_snap: int32, end_snap: int32):
            return self.getValue(NonCdbEnum.DB_TOP_SQL_SNAP_ELAPSED, NonCdbSqlSnapElapsed, 
                                dbid, begin_snap, end_snap)

    def getDbTopSqlSnapCpu(self, dbid:int64, begin_snap: int32, end_snap: int32):
            return self.getValue(NonCdbEnum.DB_TOP_SQL_SNAP_CPU, NonCdbSqlSnapCpu, 
                                dbid, begin_snap, end_snap)

    def getDbTopSqlSnapAppWait(self, dbid:int64, begin_snap: int32, end_snap: int32):
            return self.getValue(NonCdbEnum.DB_TOP_SQL_SNAP_APP_WAIT, NonCdbSqlSnapAppWait, 
                                dbid, begin_snap, end_snap)

    def getDbTopSqlSnapCcWait(self, dbid:int64, begin_snap: int32, end_snap: int32):
            return self.getValue(NonCdbEnum.DB_TOP_SQL_SNAP_CC_WAIT, NonCdbSqlSnapCcWait, 
                                dbid, begin_snap, end_snap)

    def getDbTopSqlSnapPhysicalWriteIops(self, dbid:int64, begin_snap: int32, end_snap: int32):
            return self.getValue(NonCdbEnum.DB_TOP_SQL_SNAP_PHYSICAL_WRITE_IOPS, NonCdbSqlSnapPhysicalWriteIops, 
                                dbid, begin_snap, end_snap)

    def getDbTopSqlSnapPhysicalReadIops(self, dbid:int64, begin_snap: int32, end_snap: int32):
            return self.getValue(NonCdbEnum.DB_TOP_SQL_SNAP_PHYSICAL_READ_IOPS, NonCdbSqlSnapPhysicalReadIops, 
                                dbid, begin_snap, end_snap)

    def getDbTopSqlSnapParseCall(self, dbid:int64, begin_snap: int32, end_snap: int32):
            return self.getValue(NonCdbEnum.DB_TOP_SQL_SNAP_PARSE_CALL, NonCdbSqlSnapParseCall, 
                                dbid, begin_snap, end_snap)

    def getDbTopSqlSnapLogicalRead(self, dbid:int64, begin_snap: int32, end_snap: int32):
            return self.getValue(NonCdbEnum.DB_TOP_SQL_SNAP_LOGICAL_READ, NonCdbSqlSnapLogicalRead, 
                                dbid, begin_snap, end_snap)

    def getDbTopSqlSnapPhysicalWriteMb(self, dbid:int64, begin_snap: int32, end_snap: int32):
            return self.getValue(NonCdbEnum.DB_TOP_SQL_SNAP_PHYSICAL_WRITE_MB, NonCdbSqlSnapPhysicalWriteMb, 
                                dbid, begin_snap, end_snap)

    def getDbTopSqlSnapPhysicalReadMb(self, dbid:int64, begin_snap: int32, end_snap: int32):
            return self.getValue(NonCdbEnum.DB_TOP_SQL_SNAP_PHYSICAL_READ_MB, NonCdbSqlSnapPhysicalReadMb, 
                                dbid, begin_snap, end_snap)

    def getSqlPlanChange(self, dbid:int64, begin_snap: int32, end_snap: int32):
            return self.getValue(NonCdbEnum.SQL_PLAN_CHANGE, NonCdbSqlPlanChange, 
                                dbid, begin_snap, end_snap)

    def getDbTopSqlSnapInvalid(self, dbid:int64, begin_snap: int32, end_snap: int32):
            return self.getValue(NonCdbEnum.DB_TOP_SQL_SNAP_INVALID, NonCdbSqlSnapInvalid, 
                                dbid, begin_snap, end_snap)

    def getDbTopSqlSnapDiskReads(self, dbid:int64, begin_snap: int32, end_snap: int32):
            return self.getValue(NonCdbEnum.DB_TOP_SQL_SNAP_DISK_READS, NonCdbSqlSnapDiskReads, 
                                dbid, begin_snap, end_snap)

    def getDbTopSqlPhysicalWriteIops(self, dbid:int64, begin_snap: int32, end_snap: int32):
            return self.getValue(NonCdbEnum.DB_TOP_SQL_PHYSICAL_WRITE_IOPS, OdbSqlPhysicalWriteIops, 
                                dbid, begin_snap, end_snap)

    def getDbTopSqlPhysicalReadIops(self, dbid:int64, begin_snap: int32, end_snap: int32):
            return self.getValue(NonCdbEnum.DB_TOP_SQL_PHYSICAL_READ_IOPS, OdbSqlPhysicalReadIops, 
                                dbid, begin_snap, end_snap)

    def getDbTopSqlDiskReads(self, dbid:int64, begin_snap: int32, end_snap: int32):
            return self.getValue(NonCdbEnum.DB_TOP_SQL_DISK_READS, OdbSqlDiskReads, 
                                dbid, begin_snap, end_snap)

    def getDbTopSqlLogicalRead(self, dbid:int64, begin_snap: int32, end_snap: int32):
            return self.getValue(NonCdbEnum.DB_TOP_SQL_LOGICAL_READ, OdbSqlLogicalRead, 
                                dbid, begin_snap, end_snap)

    def getDbTopSqlElapsed(self, dbid:int64, begin_snap: int32, end_snap: int32):
            return self.getValue(NonCdbEnum.DB_TOP_SQL_ELAPSED, OdbSqlElapsed, 
                                dbid, begin_snap, end_snap)

    def getDbTopSqlCwait(self, dbid:int64, begin_snap: int32, end_snap: int32):
            return self.getValue(NonCdbEnum.DB_TOP_SQL_CWAIT, OdbSqlCwait, 
                                dbid, begin_snap, end_snap)

    def getDbTopSqlIoWait(self, dbid:int64, begin_snap: int32, end_snap: int32):
            return self.getValue(NonCdbEnum.DB_TOP_SQL_IO_WAIT, OdbSqlIoWait, 
                                dbid, begin_snap, end_snap)

    def getDbTopSqlCpu(self, dbid:int64, begin_snap: int32, end_snap: int32):
            return self.getValue(NonCdbEnum.DB_TOP_SQL_CPU, OdbSqlCpu, 
                                dbid, begin_snap, end_snap)

    def getDbTopSqlParseCall(self, dbid:int64, begin_snap: int32, end_snap: int32):
            return self.getValue(NonCdbEnum.DB_TOP_SQL_PARSE_CALL, OdbSqlParseCall, 
                                dbid, begin_snap, end_snap)

    def getDbTopSqlPhysicalReadMb(self, dbid:int64, begin_snap: int32, end_snap: int32):
            return self.getValue(NonCdbEnum.DB_TOP_SQL_PHYSICAL_READ_MB, OdbSqlPhysicalReadMb, 
                                dbid, begin_snap, end_snap)

    def getDbTopSqlPhysicalWriteMb(self, dbid:int64, begin_snap: int32, end_snap: int32):
            return self.getValue(NonCdbEnum.DB_TOP_SQL_PHYSICAL_WRITE_MB, OdbSqlPhysicalWriteMb, 
                                dbid, begin_snap, end_snap)

    def getDbTopSqlOffLoad(self, dbid:int64, begin_snap: int32, end_snap: int32):
            return self.getValue(NonCdbEnum.DB_TOP_SQL_OFF_LOAD, OdbSqlOffLoad, 
                                dbid, begin_snap, end_snap)

    def getDbTopSqlOffLoadReturn(self, dbid:int64, begin_snap: int32, end_snap: int32):
            return self.getValue(NonCdbEnum.DB_TOP_SQL_OFF_LOAD_RETURN, OdbSqlOffLoadReturn, 
                                dbid, begin_snap, end_snap)

    def getDbTopSqlTotalExec(self, dbid:int64, begin_snap: int32, end_snap: int32):
            return self.getValue(NonCdbEnum.DB_TOP_SQL_TOTAL_EXEC, NonCdbSqlTotalExec, 
                                dbid, begin_snap, end_snap)

    def getDbTopSqlVersions(self, dbid:int64, begin_snap: int32, end_snap: int32):
            return self.getValue(NonCdbEnum.DB_TOP_SQL_VERSIONS, OdbSqlVersions, 
                                dbid, begin_snap, end_snap)

    def getResourceLimit(self, dbid:int64, begin_snap: int32, end_snap: int32):
            return self.getValue(NonCdbEnum.RESOURCE_LIMIT, OdbResourceLimit, 
                                dbid, begin_snap, end_snap)

    def getExaCellServerIoStatistic(self, dbid:int64, begin_snap: int32, end_snap: int32):
            return self.getValue(NonCdbEnum.EXA_CELL_SERVER_IO_STATISTIC, OdbExaCellServerIoStatistic, 
                                dbid, begin_snap, end_snap)

    def getExaCellServerIoStatisticCell(self, dbid:int64, begin_snap: int32, end_snap: int32):
            return self.getValue(NonCdbEnum.EXA_CELL_SERVER_IO_STATISTIC_CELL, OdbExaCellServerIoStatisticCell, 
                                dbid, begin_snap, end_snap)

    def getExaTopDatabaseIoStatistic(self, dbid:int64, begin_snap: int32, end_snap: int32):
            return self.getValue(NonCdbEnum.EXA_TOP_DATABASE_IO_STATISTIC, OdbExaTopDatabaseIoStatistic, 
                                dbid, begin_snap, end_snap)

    def getExaDatabaseSystat(self, dbid:int64, begin_snap: int32, end_snap: int32):
            return self.getValue(NonCdbEnum.EXA_DATABASE_SYSTAT, OdbExaDatabaseSystat, 
                                dbid, begin_snap, end_snap)

    def getExaCellSummary(self, dbid:int64, begin_snap: int32, end_snap: int32):
            return self.getValue(NonCdbEnum.EXA_CELL_SUMMARY, OdbExaCellSummary, 
                                dbid, begin_snap, end_snap)

    def getExaCellGlobalCell(self, dbid:int64, begin_snap: int32, end_snap: int32):
            return self.getValue(NonCdbEnum.EXA_CELL_GLOBAL_CELL, OdbExaCellGlobalCell, 
                                dbid, begin_snap, end_snap)

    def getExaCellGlobal(self, dbid:int64, begin_snap: int32, end_snap: int32):
            return self.getValue(NonCdbEnum.EXA_CELL_GLOBAL, OdbExaCellGlobal, 
                                dbid, begin_snap, end_snap)

    def getExaIoReason(self, dbid:int64, begin_snap: int32, end_snap: int32):
            return self.getValue(NonCdbEnum.EXA_IO_REASON, OdbExaIoReason, 
                                dbid, begin_snap, end_snap)

    def getExaCellAlert(self, dbid:int64, begin_snap: int32, end_snap: int32):
            return self.getValue(NonCdbEnum.EXA_CELL_ALERT, OdbExaCellAlert, 
                                dbid, begin_snap, end_snap)

    def getDbaHistoryStatisticGlobal(self, dbid:int64, begin_snap: int32, end_snap: int32):
            return self.getValue(NonCdbEnum.DBA_HISTORY_STATISTIC_GLOBAL, OdbDbaHistoryStatisticGlobal, 
                                dbid, begin_snap, end_snap)

    def getDbSqlFullScan(self, dbid:int64, begin_snap: int32, end_snap: int32):
            return self.getValue(NonCdbEnum.DB_SQL_FULL_SCAN, NonCdbSqlFullScan, 
                                dbid, begin_snap, end_snap)

    def getAwrAshOverallWaitClass(self, dbid:int64, begin_snap: int32, end_snap: int32):
            return self.getValue(NonCdbEnum.AWR_ASH_OVERALL_WAIT_CLASS, NonCdbAwrAshOverallWaitClass, 
                                dbid, begin_snap, end_snap)

    def getAwrAshOverallEvent(self, dbid:int64, begin_snap: int32, end_snap: int32):
            return self.getValue(NonCdbEnum.AWR_ASH_OVERALL_EVENT, NonCdbAwrAshOverallEvent, 
                                dbid, begin_snap, end_snap)

    def getAwrAshOverallModule(self, dbid:int64, begin_snap: int32, end_snap: int32):
            return self.getValue(NonCdbEnum.AWR_ASH_OVERALL_MODULE, NonCdbAwrAshOverallModule, 
                                dbid, begin_snap, end_snap)

    def getAwrAshOverallProgram(self, dbid:int64, begin_snap: int32, end_snap: int32):
            return self.getValue(NonCdbEnum.AWR_ASH_OVERALL_PROGRAM, NonCdbAwrAshOverallProgram, 
                                dbid, begin_snap, end_snap)

    def getAwrAshOverallSegment(self, dbid:int64, begin_snap: int32, end_snap: int32):
            return self.getValue(NonCdbEnum.AWR_ASH_OVERALL_SEGMENT, NonCdbAwrAshOverallSegment, 
                                dbid, begin_snap, end_snap)

    def getAwrAshOverallIndex(self, dbid:int64, begin_snap: int32, end_snap: int32):
            return self.getValue(NonCdbEnum.AWR_ASH_OVERALL_INDEX, NonCdbAwrAshOverallIndex, 
                                dbid, begin_snap, end_snap)

    def getAwrAshOverallTable(self, dbid:int64, begin_snap: int32, end_snap: int32):
            return self.getValue(NonCdbEnum.AWR_ASH_OVERALL_TABLE, NonCdbAwrAshOverallTable, 
                                dbid, begin_snap, end_snap)

    def getAwrAshOverallSql(self, dbid:int64, begin_snap: int32, end_snap: int32):
            return self.getValue(NonCdbEnum.AWR_ASH_OVERALL_SQL, NonCdbAwrAshOverallSql, 
                                dbid, begin_snap, end_snap)

    def getAwrAshOverallSqlCpu(self, dbid:int64, begin_snap: int32, end_snap: int32):
            return self.getValue(NonCdbEnum.AWR_ASH_OVERALL_SQL_CPU, NonCdbAwrAshOverallSql, 
                                dbid, begin_snap, end_snap)

    def getAwrAshOverallSqlIo(self, dbid:int64, begin_snap: int32, end_snap: int32):
            return self.getValue(NonCdbEnum.AWR_ASH_OVERALL_SQL_IO, NonCdbAwrAshOverallSql, 
                                dbid, begin_snap, end_snap)

    def getAwrAshOverallSqlWait(self, dbid:int64, begin_snap: int32, end_snap: int32):
            return self.getValue(NonCdbEnum.AWR_ASH_OVERALL_SQL_WAIT, NonCdbAwrAshOverallSql, 
                                dbid, begin_snap, end_snap)

    def getAshOverallSqlOperation(self, dbid:int64, begin_snap: int32, end_snap: int32):
            return self.getValue(NonCdbEnum.ASH_OVERALL_SQL_OPERATION, OdbAshOverallSqlOperation, 
                                dbid, begin_snap, end_snap)

    def getAwrAasGraph(self, dbid:int64, begin_snap: int32, end_snap: int32):
            return self.getValue(NonCdbEnum.AWR_AAS_GRAPH, OdbAwrAasGraph, 
                                dbid, begin_snap, end_snap)

    def getAwrAasGraphGlobal(self, dbid:int64, begin_snap: int32, end_snap: int32):
            return self.getValue(NonCdbEnum.AWR_AAS_GRAPH_GLOBAL, OdbAwrAasGraphGlobal, 
                                dbid, begin_snap, end_snap)

    def getExaAsmDiskgroup(self, dbid:int64, begin_snap: int32, end_snap: int32):
            return self.getValue(NonCdbEnum.EXA_ASM_DISKGROUP, OdbExaAsmDiskgroup, 
                                dbid, begin_snap, end_snap)

    def getGcBlockSrvGraph(self, dbid:int64, begin_snap: int32, end_snap: int32):
            return self.getValue(NonCdbEnum.GC_BLOCK_SRV_GRAPH, OdbGcBlockSrvGraph, 
                                dbid, begin_snap, end_snap)

    def getIoFunctionStatistic(self, dbid:int64, begin_snap: int32, end_snap: int32):
            return self.getValue(NonCdbEnum.IO_FUNCTION_STATISTIC, OdbIoFunctionStatistic, 
                                dbid, begin_snap, end_snap)

    def getIoFunctionStatisticGlobal(self, dbid:int64, begin_snap: int32, end_snap: int32):
            return self.getValue(NonCdbEnum.IO_FUNCTION_STATISTIC_GLOBAL, OdbIoFunctionStatisticGlobal, 
                                dbid, begin_snap, end_snap)

    def getPgaEffStatistic(self, dbid:int64, begin_snap: int32, end_snap: int32):
            return self.getValue(NonCdbEnum.PGA_EFF_STATISTIC, OdbPgaEffStatistic, 
                                dbid, begin_snap, end_snap)

    def getTimeModelStatistic(self, dbid:int64, begin_snap: int32, end_snap: int32):
            return self.getValue(NonCdbEnum.TIME_MODEL_STATISTIC, NonCdbTimeModelStatistic, 
                                dbid, begin_snap, end_snap)

    def getSgaStatistic(self, dbid:int64, begin_snap: int32, end_snap: int32):
            return self.getValue(NonCdbEnum.SGA_STATISTIC, OdbSgaStatistic, 
                                dbid, begin_snap, end_snap)

    def getGcEfficientGraph(self, dbid:int64, begin_snap: int32, end_snap: int32):
            return self.getValue(NonCdbEnum.GC_EFFICIENT_GRAPH, OdbGcEfficientGraph, 
                                dbid, begin_snap, end_snap)

    def getMemConfig(self, dbid:int64, begin_snap: int32, end_snap: int32):
            return self.getValue(NonCdbEnum.MEM_CONFIG, OdbMemConfig, 
                                dbid, begin_snap, end_snap)

    def getBufferPoolConfig(self, dbid:int64, begin_snap: int32, end_snap: int32):
            return self.getValue(NonCdbEnum.BUFFER_POOL_CONFIG, OdbBufferPoolConfig, 
                                dbid, begin_snap, end_snap)

    def getMetricStatistic(self, dbid:int64, begin_snap: int32, end_snap: int32):
            return self.getValue(NonCdbEnum.METRIC_STATISTIC, OdbMetricStatistic, 
                                dbid, begin_snap, end_snap)

    def getGcLoadProfile(self, dbid:int64, begin_snap: int32, end_snap: int32):
            return self.getValue(NonCdbEnum.GC_LOAD_PROFILE, OdbGcLoadProfile, 
                                dbid, begin_snap, end_snap)

    def getUndoConfig(self, dbid:int64, begin_snap: int32, end_snap: int32):
            return self.getValue(NonCdbEnum.UNDO_CONFIG, NonCdbUndoConfig, 
                                dbid, begin_snap, end_snap)

    def getTbsIoStatistic(self, dbid:int64, begin_snap: int32, end_snap: int32):
            return self.getValue(NonCdbEnum.TBS_IO_STATISTIC, OdbTbsIoStatistic, 
                                dbid, begin_snap, end_snap)

    def getGcWorkload(self, dbid:int64, begin_snap: int32, end_snap: int32):
            return self.getValue(NonCdbEnum.GC_WORKLOAD, OdbGcWorkload, 
                                dbid, begin_snap, end_snap)

    def getDbTopSegmentPhysicalWriteIops(self, dbid:int64, begin_snap: int32, end_snap: int32):
            return self.getValue(NonCdbEnum.DB_TOP_SEGMENT_PHYSICAL_WRITE_IOPS, OdbSegmentPhysicalWriteIops, 
                                dbid, begin_snap, end_snap)

    def getDbTopSegmentPhysicalWriteDir(self, dbid:int64, begin_snap: int32, end_snap: int32):
            return self.getValue(NonCdbEnum.DB_TOP_SEGMENT_PHYSICAL_WRITE_DIR, OdbSegmentPhysicalWriteDir, 
                                dbid, begin_snap, end_snap)

    def getDbTopSegmentRowLock(self, dbid:int64, begin_snap: int32, end_snap: int32):
            return self.getValue(NonCdbEnum.DB_TOP_SEGMENT_ROW_LOCK, OdbSegmentRowLock, 
                                dbid, begin_snap, end_snap)

    def getDbTopSegmentPhysicalWrite(self, dbid:int64, begin_snap: int32, end_snap: int32):
            return self.getValue(NonCdbEnum.DB_TOP_SEGMENT_PHYSICAL_WRITE, OdbSegmentPhysicalWrite, 
                                dbid, begin_snap, end_snap)

    def getDbTopSegmentPhysicalReadIops(self, dbid:int64, begin_snap: int32, end_snap: int32):
            return self.getValue(NonCdbEnum.DB_TOP_SEGMENT_PHYSICAL_READ_IOPS, OdbSegmentPhysicalReadIops, 
                                dbid, begin_snap, end_snap)

    def getDbTopSegmentPhysicalReadDir(self, dbid:int64, begin_snap: int32, end_snap: int32):
            return self.getValue(NonCdbEnum.DB_TOP_SEGMENT_PHYSICAL_READ_DIR, OdbSegmentPhysicalReadDir, 
                                dbid, begin_snap, end_snap)

    def getDbTopSegmentPhysicalRead(self, dbid:int64, begin_snap: int32, end_snap: int32):
            return self.getValue(NonCdbEnum.DB_TOP_SEGMENT_PHYSICAL_READ, OdbSegmentPhysicalRead, 
                                dbid, begin_snap, end_snap)

    def getDbTopSegmentOptPhysicalRead(self, dbid:int64, begin_snap: int32, end_snap: int32):
            return self.getValue(NonCdbEnum.DB_TOP_SEGMENT_OPT_PHYSICAL_READ, OdbSegmentOptPhysicalRead, 
                                dbid, begin_snap, end_snap)

    def getDbTopSegmentLogicalRead(self, dbid:int64, begin_snap: int32, end_snap: int32):
            return self.getValue(NonCdbEnum.DB_TOP_SEGMENT_LOGICAL_READ, OdbSegmentLogicalRead, 
                                dbid, begin_snap, end_snap)

    def getDbTopSegmentItlWaits(self, dbid:int64, begin_snap: int32, end_snap: int32):
            return self.getValue(NonCdbEnum.DB_TOP_SEGMENT_ITL_WAITS, OdbSegmentItlWaits, 
                                dbid, begin_snap, end_snap)

    def getDbTopSegmentGcCurrentBlockSrv(self, dbid:int64, begin_snap: int32, end_snap: int32):
            return self.getValue(NonCdbEnum.DB_TOP_SEGMENT_GC_CURRENT_BLOCK_SRV, OdbSegmentGcCurrentBlockSrv, 
                                dbid, begin_snap, end_snap)

    def getDbTopSegmentGcCurrentBlockRec(self, dbid:int64, begin_snap: int32, end_snap: int32):
            return self.getValue(NonCdbEnum.DB_TOP_SEGMENT_GC_CURRENT_BLOCK_REC, OdbSegmentGcCurrentBlockRec, 
                                dbid, begin_snap, end_snap)

    def getDbTopSegmentGcCrBlockSrv(self, dbid:int64, begin_snap: int32, end_snap: int32):
            return self.getValue(NonCdbEnum.DB_TOP_SEGMENT_GC_CR_BLOCK_SRV, OdbSegmentGcCrBlockSrv, 
                                dbid, begin_snap, end_snap)

    def getDbTopSegmentGcCrBlockRec(self, dbid:int64, begin_snap: int32, end_snap: int32):
            return self.getValue(NonCdbEnum.DB_TOP_SEGMENT_GC_CR_BLOCK_REC, OdbSegmentGcCrBlockRec, 
                                dbid, begin_snap, end_snap)

    def getDbTopSegmentGcBufferBusyWait(self, dbid:int64, begin_snap: int32, end_snap: int32):
            return self.getValue(NonCdbEnum.DB_TOP_SEGMENT_GC_BUFFER_BUSY_WAIT, OdbSegmentGcBufferBusyWait, 
                                dbid, begin_snap, end_snap)

    def getDbTopSegmentChainRow(self, dbid:int64, begin_snap: int32, end_snap: int32):
            return self.getValue(NonCdbEnum.DB_TOP_SEGMENT_CHAIN_ROW, OdbSegmentChainRow, 
                                dbid, begin_snap, end_snap)

    def getDbTopSegmentBufferBusyWait(self, dbid:int64, begin_snap: int32, end_snap: int32):
            return self.getValue(NonCdbEnum.DB_TOP_SEGMENT_BUFFER_BUSY_WAIT, OdbSegmentBufferBusyWait, 
                                dbid, begin_snap, end_snap)

    def getDbTopSegmentBlockChange(self, dbid:int64, begin_snap: int32, end_snap: int32):
            return self.getValue(NonCdbEnum.DB_TOP_SEGMENT_BLOCK_CHANGE, OdbSegmentBlockChange, 
                                dbid, begin_snap, end_snap)

    def getDbTopSegmentTableScans(self, dbid:int64, begin_snap: int32, end_snap: int32):
            return self.getValue(NonCdbEnum.DB_TOP_SEGMENT_TABLE_SCANS, OdbSegmentTableScans, 
                                dbid, begin_snap, end_snap)

    def getGcEnqueueMessaging(self, dbid:int64, begin_snap: int32, end_snap: int32):
            return self.getValue(NonCdbEnum.GC_ENQUEUE_MESSAGING, OdbGcEnqueueMessaging, 
                                dbid, begin_snap, end_snap)

    def getDbTopSegmentSnapPhysicalWriteIops(self, dbid:int64, begin_snap: int32, end_snap: int32):
            return self.getValue(NonCdbEnum.DB_TOP_SEGMENT_SNAP_PHYSICAL_WRITE_IOPS, NonCdbSegmentSnapPhysicalWriteIops, 
                                dbid, begin_snap, end_snap)

    def getDbTopSegmentSnapPhysicalWriteDir(self, dbid:int64, begin_snap: int32, end_snap: int32):
            return self.getValue(NonCdbEnum.DB_TOP_SEGMENT_SNAP_PHYSICAL_WRITE_DIR, NonCdbSegmentSnapPhysicalWriteDir, 
                                dbid, begin_snap, end_snap)

    def getDbTopSegmentSnapTableScans(self, dbid:int64, begin_snap: int32, end_snap: int32):
            return self.getValue(NonCdbEnum.DB_TOP_SEGMENT_SNAP_TABLE_SCANS, NonCdbSegmentSnapTableScans, 
                                dbid, begin_snap, end_snap)

    def getDbTopSegmentSnapRowLock(self, dbid:int64, begin_snap: int32, end_snap: int32):
            return self.getValue(NonCdbEnum.DB_TOP_SEGMENT_SNAP_ROW_LOCK, NonCdbSegmentSnapRowLock, 
                                dbid, begin_snap, end_snap)

    def getMemResize(self, dbid:int64, begin_snap: int32, end_snap: int32):
            return self.getValue(NonCdbEnum.MEM_RESIZE, NonCdbMemResize, 
                                dbid, begin_snap, end_snap)

    def getDbTopSegmentSnapPhysicalWrite(self, dbid:int64, begin_snap: int32, end_snap: int32):
            return self.getValue(NonCdbEnum.DB_TOP_SEGMENT_SNAP_PHYSICAL_WRITE, NonCdbSegmentSnapPhysicalWrite, 
                                dbid, begin_snap, end_snap)

    def getDbTopSegmentSnapPhysicalReadIops(self, dbid:int64, begin_snap: int32, end_snap: int32):
            return self.getValue(NonCdbEnum.DB_TOP_SEGMENT_SNAP_PHYSICAL_READ_IOPS, NonCdbSegmentSnapPhysicalReadIops, 
                                dbid, begin_snap, end_snap)

    def getDbTopSegmentSnapPhysicalReadDir(self, dbid:int64, begin_snap: int32, end_snap: int32):
            return self.getValue(NonCdbEnum.DB_TOP_SEGMENT_SNAP_PHYSICAL_READ_DIR, NonCdbSegmentSnapPhysicalReadDir, 
                                dbid, begin_snap, end_snap)

    def getDbTopSegmentSnapPhysicalRead(self, dbid:int64, begin_snap: int32, end_snap: int32):
            return self.getValue(NonCdbEnum.DB_TOP_SEGMENT_SNAP_PHYSICAL_READ, NonCdbSegmentSnapPhysicalRead, 
                                dbid, begin_snap, end_snap)

    def getDbTopSegmentSnapOptPhysicalRead(self, dbid:int64, begin_snap: int32, end_snap: int32):
            return self.getValue(NonCdbEnum.DB_TOP_SEGMENT_SNAP_OPT_PHYSICAL_READ, NonCdbSegmentSnapOptPhysicalRead, 
                                dbid, begin_snap, end_snap)

    def getDbTopSegmentSnapLogicalRead(self, dbid:int64, begin_snap: int32, end_snap: int32):
            return self.getValue(NonCdbEnum.DB_TOP_SEGMENT_SNAP_LOGICAL_READ, NonCdbSegmentSnapLogicalRead, 
                                dbid, begin_snap, end_snap)

    def getDbTopSegmentSnapItlWaits(self, dbid:int64, begin_snap: int32, end_snap: int32):
            return self.getValue(NonCdbEnum.DB_TOP_SEGMENT_SNAP_ITL_WAITS, NonCdbSegmentSnapItlWaits, 
                                dbid, begin_snap, end_snap)

    def getDbTopSegmentSnapGcCurrentBlockSrv(self, dbid:int64, begin_snap: int32, end_snap: int32):
            return self.getValue(NonCdbEnum.DB_TOP_SEGMENT_SNAP_GC_CURRENT_BLOCK_SRV, NonCdbSegmentSnapGcCurrentBlockSrv, 
                                dbid, begin_snap, end_snap)

    def getDbTopSegmentSnapGcCurrentBlockRec(self, dbid:int64, begin_snap: int32, end_snap: int32):
            return self.getValue(NonCdbEnum.DB_TOP_SEGMENT_SNAP_GC_CURRENT_BLOCK_REC, NonCdbSegmentSnapGcCurrentBlockRec, 
                                dbid, begin_snap, end_snap)

    def getDbTopSegmentSnapGcCrBlockSrv(self, dbid:int64, begin_snap: int32, end_snap: int32):
            return self.getValue(NonCdbEnum.DB_TOP_SEGMENT_SNAP_GC_CR_BLOCK_SRV, NonCdbSegmentSnapGcCrBlockSrv, 
                                dbid, begin_snap, end_snap)

    def getDbTopSegmentSnapGcCrBlockRec(self, dbid:int64, begin_snap: int32, end_snap: int32):
            return self.getValue(NonCdbEnum.DB_TOP_SEGMENT_SNAP_GC_CR_BLOCK_REC, NonCdbSegmentSnapGcCrBlockRec, 
                                dbid, begin_snap, end_snap)

    def getDbTopSegmentSnapGcBufferBusyWait(self, dbid:int64, begin_snap: int32, end_snap: int32):
            return self.getValue(NonCdbEnum.DB_TOP_SEGMENT_SNAP_GC_BUFFER_BUSY_WAIT, NonCdbSegmentSnapGcBufferBusyWait, 
                                dbid, begin_snap, end_snap)

    def getDbTopSegmentSnapChainRow(self, dbid:int64, begin_snap: int32, end_snap: int32):
            return self.getValue(NonCdbEnum.DB_TOP_SEGMENT_SNAP_CHAIN_ROW, NonCdbSegmentSnapChainRow, 
                                dbid, begin_snap, end_snap)

    def getDbTopSegmentSnapBufferBusyWait(self, dbid:int64, begin_snap: int32, end_snap: int32):
            return self.getValue(NonCdbEnum.DB_TOP_SEGMENT_SNAP_BUFFER_BUSY_WAIT, NonCdbSegmentSnapBufferBusyWait, 
                                dbid, begin_snap, end_snap)

    def getDbTopSegmentSnapBlockChange(self, dbid:int64, begin_snap: int32, end_snap: int32):
            return self.getValue(NonCdbEnum.DB_TOP_SEGMENT_SNAP_BLOCK_CHANGE, NonCdbSegmentSnapBlockChange, 
                                dbid, begin_snap, end_snap)

    '''extract top sql'''
    def getExtractTopSqlCpu(self, top_n_rows: int = 10):
            return self.extractTopSql(NonCdbEnum.EXTRACT_TOP_SQL_CPU, top_n_rows)

    def getExtractTopSqlWait(self,  top_n_rows: int = 10):
            return self.extractTopSql(NonCdbEnum.EXTRACT_TOP_SQL_WAIT, top_n_rows)

    def getExtractTopsqlIo(self,  top_n_rows: int = 10):
            return self.extractTopSql(NonCdbEnum.EXTRACT_TOPSQL_IO, top_n_rows)
