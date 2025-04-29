from numpy import int32, int64
from data.db_context import DbContext, DataOperators
from app.data.repositories.general_repository import GeneralRepository
from logger import AppLogger
# from app.data.repositories.enum.cdb_enum import CdbEnum
from app.data.models.cdb_model import *

    
class CdbAshOverallRepository(GeneralRepository):
    
    _logger = AppLogger().get_logger()
    
    def __init__(self, db_context: DbContext):
        
        if not isinstance(db_context, DataOperators):
            self._logger.error(TypeError("db_context must implement DataOperations"))        
        self.db_context = db_context
    
    async def ash_overall_index(self, cus_code: str, dbid: int64, begin_snap: int32, end_snap: int32):
        query = """SELECT DBID, A.INSTANCE_NAME , DB_NAME, A.PDB_NAME , OWNER, OBJECT_NAME, A.PCT 
        FROM (SELECT A.DBID, A.INSTANCE_NAME, A.DB_NAME , A.PDB_NAME , A.OWNER , A.OBJECT_NAME, 
                ROUND(SUM(TIME_WAITED) * 100 / NULLIF(SUM(SUM(TIME_WAITED)) OVER (PARTITION BY A.DBID, A.INSTANCE_NUMBER),0), 2) PCT 
            FROM CDB_ASH_OVERALL_OBJECTS A 
            WHERE CUS_CODE = :P_CUS_CODE 
                AND A.DBID = :P_DBID AND A.SNAP_ID BETWEEN :P_BEGIN_SNAP AND :P_END_SNAP  
                AND A.OBJECT_TYPE  = 'INDEX' 
            GROUP BY  A.DBID, A.INSTANCE_NAME, A.DB_NAME , A.PDB_NAME , A.OWNER , A.OBJECT_NAME ,A.INSTANCE_NUMBER ) A 
        WHERE A.PCT  > 1 
        ORDER BY DB_NAME,INSTANCE_NAME,PCT DESC, OBJECT_NAME"""
        data = await self.get_data(query, AshOverallObject, cus_code, dbid, begin_snap, end_snap)
        return data

    async def ash_overall_table(self, cus_code: str, dbid: int64, begin_snap: int32, end_snap: int32):
        query = """SELECT DBID, A.INSTANCE_NAME , DB_NAME, A.PDB_NAME , OWNER, OBJECT_NAME, A.PCT 
        FROM (SELECT A.DBID, A.INSTANCE_NAME, A.DB_NAME , A.PDB_NAME , A.OWNER , A.OBJECT_NAME, 
                ROUND(SUM(TIME_WAITED) * 100 / NULLIF(SUM(SUM(TIME_WAITED)) OVER (PARTITION BY A.DBID, A.INSTANCE_NUMBER),0), 2) PCT 
            FROM CDB_ASH_OVERALL_OBJECTS A 
            WHERE CUS_CODE = :P_CUS_CODE 
                AND A.DBID = :P_DBID AND A.SNAP_ID BETWEEN :P_BEGIN_SNAP AND :P_END_SNAP  
                AND A.OBJECT_TYPE  = 'TABLE' 
            GROUP BY  A.DBID, A.INSTANCE_NAME, A.DB_NAME , A.PDB_NAME , A.OWNER , A.OBJECT_NAME ,A.INSTANCE_NUMBER ) A 
        WHERE A.PCT  > 1 
        ORDER BY DB_NAME,INSTANCE_NAME,PCT DESC, OBJECT_NAME"""
        data = await self.get_data(query, AshOverallObject, cus_code, dbid, begin_snap, end_snap)
        return data
    
    async def ash_overall_segment(self, cus_code: str, dbid: int64, begin_snap: int32, end_snap: int32):
        query = """SELECT DBID, A.INSTANCE_NAME , DB_NAME, A.PDB_NAME , OWNER, OBJECT_NAME, A.PCT 
        FROM (SELECT A.DBID, A.INSTANCE_NAME, A.DB_NAME , A.PDB_NAME , A.OWNER , A.OBJECT_NAME, 
                ROUND(SUM(TIME_WAITED) * 100 / NULLIF(SUM(SUM(TIME_WAITED)) OVER (PARTITION BY A.DBID, A.INSTANCE_NUMBER),0), 2) PCT 
            FROM CDB_ASH_OVERALL_OBJECTS A 
            WHERE CUS_CODE = :P_CUS_CODE 
                AND A.DBID = :P_DBID AND A.SNAP_ID BETWEEN :P_BEGIN_SNAP AND :P_END_SNAP  
            GROUP BY  A.DBID, A.INSTANCE_NAME, A.DB_NAME , A.PDB_NAME , A.OWNER , A.OBJECT_NAME ,A.INSTANCE_NUMBER ) A 
        WHERE A.PCT  > 1 
        ORDER BY DB_NAME,INSTANCE_NAME,PCT DESC, OBJECT_NAME"""
        data = await self.get_data(query, AshOverallObject, cus_code, dbid, begin_snap, end_snap)
        return data
    
    async def ash_overall_sql_cpu(self, cus_code: str, dbid: int64, begin_snap: int32, end_snap: int32):
        query = """select a.cus_code, a.dbid, a.instance_number, instance_name, db_name, pdb_name, sql_id, pct  
            from ( select cus_code, dbid, instance_number,instance_name, db_name, pdb_name, sql_id, 
                        ROUND((RATIO_TO_REPORT(COUNT(*)) OVER (PARTITION BY A.DBID,A.INSTANCE_NUMBER))*100,2) PCT 
                    from cdb_ash_overall_items a 
                    where cus_code = :P_CUS_CODE  and a.dbid = :P_DBID and a.snap_id between :P_BEGIN_SNAP and :P_END_SNAP group by cus_code, dbid,instance_number,instance_name, db_name, cus_code,  pdb_name, sql_id ) a 
            where pct>1 order by instance_name, pct DESC"""
        data = await self.get_data(query, AshOverallSql, cus_code, dbid, begin_snap, end_snap)
        return data
    
    async def ash_overall_sql_io(self, cus_code: str, dbid: int64, begin_snap: int32, end_snap: int32):
        query = """ SELECT DBID, INSTANCE_NUMBER, instance_name, DB_NAME , pdb_name, sql_id, PCT 
            FROM (SELECT DBID, INSTANCE_NUMBER, instance_name, caoi.DB_NAME , pdb_name, sql_id, 
                ROUND((RATIO_TO_REPORT(COUNT(*)) OVER (PARTITION BY DBID, INSTANCE_NUMBER))*100,2)  PCT 
                FROM CDB_ASH_OVERALL_ITEMS caoi 
                WHERE CUS_CODE = :P_CUS_CODE  AND caoi.DBID = :P_DBID AND caoi.SNAP_ID BETWEEN :P_BEGIN_SNAP AND :P_END_SNAP 
                    AND caoi.SQL_ID IS NOT NULL AND session_state = 'WAITING' AND caoi.WAIT_CLASS = 'User I/O' 
                    GROUP BY instance_name, caoi.DB_NAME , pdb_name, caoi.sql_id, DBID, INSTANCE_NUMBER) a 
            WHERE a.PCT > 1 ORDER BY instance_name, pct DESC
            """
        data = await self.get_data(query, AshOverallSql, cus_code, dbid, begin_snap, end_snap)
        return data

    async def ash_overall_sql_wait(self, cus_code: str, dbid: int64, begin_snap: int32, end_snap: int32):
        query = """ SELECT DBID, INSTANCE_NUMBER, instance_name, DB_NAME , pdb_name, sql_id, PCT FROM (SELECT DBID, INSTANCE_NUMBER, instance_name, caoi.DB_NAME , pdb_name, sql_id,  ROUND((RATIO_TO_REPORT(COUNT(*)) OVER (PARTITION BY DBID, INSTANCE_NUMBER))*100,2)  PCT FROM CDB_ASH_OVERALL_ITEMS caoi WHERE CUS_CODE = :P_CUS_CODE  AND caoi.DBID = :P_DBID AND caoi.SNAP_ID BETWEEN :P_BEGIN_SNAP AND :P_END_SNAP AND caoi.SQL_ID IS NOT NULL AND session_state = 'WAITING' AND caoi.WAIT_CLASS != 'User I/O' GROUP BY instance_name, caoi.DB_NAME , pdb_name, caoi.sql_id, DBID, INSTANCE_NUMBER) a WHERE a.PCT > 1 ORDER BY instance_name, pct DESC
            """
        data = await self.get_data(query, AshOverallSql, cus_code, dbid, begin_snap, end_snap)
        return data
    
    async def ash_overall_wait_class(self, cus_code: str, dbid: int64, begin_snap: int32, end_snap: int32):
        query = """SELECT DBID, INSTANCE_NUMBER, instance_name, DB_NAME , pdb_name, WAIT_CLASS, PCT 
        FROM (SELECT DBID, INSTANCE_NUMBER, instance_name, caoi.DB_NAME , pdb_name, caoi.WAIT_CLASS,
        ROUND((RATIO_TO_REPORT(COUNT(*)) OVER (PARTITION BY caoi.DBID, caoi.INSTANCE_NUMBER))*100,2) pct 
        FROM CDB_ASH_OVERALL_ITEMS caoi 
        WHERE CUS_CODE = :P_CUS_CODE  AND caoi.DBID = :P_DBID AND caoi.SNAP_ID BETWEEN :P_BEGIN_SNAP AND :P_END_SNAP 
        GROUP BY instance_name, caoi.DB_NAME , pdb_name, caoi.WAIT_CLASS, DBID, INSTANCE_NUMBER) a WHERE a.PCT > 1 
        ORDER BY instance_name,pct DESC
            """
        data = await self.get_data(query, AshOverallWaitClass, cus_code, dbid, begin_snap, end_snap)
        
        return data
    
    async def ash_overall_event(self, cus_code: str, dbid: int64, begin_snap: int32, end_snap: int32):
        query = """SELECT DBID, INSTANCE_NUMBER, instance_name, DB_NAME , pdb_name, EVENT, PCT FROM (SELECT DBID, INSTANCE_NUMBER, instance_name, caoi.DB_NAME , pdb_name, caoi.EVENT, ROUND((RATIO_TO_REPORT(COUNT(*)) OVER (PARTITION BY caoi.DBID, caoi.INSTANCE_NUMBER))*100,2) pct FROM CDB_ASH_OVERALL_ITEMS caoi  WHERE CUS_CODE = :P_CUS_CODE  AND caoi.DBID = :P_DBID AND caoi.SNAP_ID BETWEEN :P_BEGIN_SNAP AND :P_END_SNAP GROUP BY instance_name, caoi.DB_NAME , pdb_name, caoi.EVENT, DBID, INSTANCE_NUMBER) a WHERE a.PCT > 1 ORDER BY instance_name,pct DESC
            """
        data = await self.get_data(query, AshOverallEvent, cus_code, dbid, begin_snap, end_snap)
        return data
    
    async def ash_overall_module(self, cus_code: str, dbid: int64, begin_snap: int32, end_snap: int32):
        query = """ SELECT DBID, INSTANCE_NUMBER, instance_name, DB_NAME , pdb_name, module, PCT FROM (SELECT DBID, INSTANCE_NUMBER, instance_name, caoi.DB_NAME , pdb_name, caoi.module, ROUND((RATIO_TO_REPORT(COUNT(*)) OVER (PARTITION BY DBID, INSTANCE_NUMBER))*100,2) pct FROM CDB_ASH_OVERALL_ITEMS caoi WHERE CUS_CODE = :P_CUS_CODE  AND caoi.DBID = :P_DBID AND caoi.SNAP_ID BETWEEN :P_BEGIN_SNAP AND :P_END_SNAP GROUP BY instance_name, caoi.DB_NAME , pdb_name, caoi.module, DBID, INSTANCE_NUMBER) a WHERE a.PCT > 1 ORDER BY instance_name,pct DESC
            """
        data = await self.get_data(query, AshOverallModule, cus_code, dbid, begin_snap, end_snap)
        return data
    
    async def ash_overall_program(self, cus_code: str, dbid: int64, begin_snap: int32, end_snap: int32):
        query = """ SELECT DBID, INSTANCE_NUMBER, instance_name, DB_NAME , pdb_name, PROGRAM, PCT FROM (SELECT DBID, INSTANCE_NUMBER, instance_name, caoi.DB_NAME , pdb_name, caoi.PROGRAM, ROUND((RATIO_TO_REPORT(COUNT(*)) OVER (PARTITION BY DBID, INSTANCE_NUMBER))*100,2) PCT FROM CDB_ASH_OVERALL_ITEMS caoi WHERE CUS_CODE = :P_CUS_CODE  AND caoi.DBID = :P_DBID AND caoi.SNAP_ID BETWEEN :P_BEGIN_SNAP AND :P_END_SNAP GROUP BY instance_name, caoi.DB_NAME , pdb_name, caoi.PROGRAM, DBID, INSTANCE_NUMBER) a WHERE a.PCT > 1 ORDER BY instance_name, pct DESC
            """
        data = await self.get_data(query, AshOverallProgram, cus_code, dbid, begin_snap, end_snap)
        return data
    
    async def ash_overall_sql_operation(self, cus_code: str, dbid: int64, begin_snap: int32, end_snap: int32):
        query = """SELECT DBID, INSTANCE_NUMBER, instance_name, DB_NAME , pdb_name, operation, PCT FROM (SELECT DBID, INSTANCE_NUMBER, instance_name, caoi.DB_NAME , pdb_name, SUBSTR(sql_plan_operation||' '||sql_plan_options, 1, 40) operation,ROUND((RATIO_TO_REPORT(COUNT(*)) OVER (PARTITION BY DBID, INSTANCE_NUMBER))*100,2)  PCT FROM CDB_ASH_OVERALL_ITEMS caoi WHERE CUS_CODE = :P_CUS_CODE  AND caoi.DBID = :P_DBID AND caoi.SNAP_ID BETWEEN :P_BEGIN_SNAP AND :P_END_SNAP and sql_plan_operation IS NOT NULL and SQL_ID is not NULL GROUP BY instance_name, caoi.DB_NAME , pdb_name, DBID, INSTANCE_NUMBER, SUBSTR(sql_plan_operation||' '||sql_plan_options, 1, 40)) a WHERE a.PCT > 1 ORDER BY instance_name, pct DESC
            """
        data = await self.get_data(query, AshOverallSqlOperation, cus_code, dbid, begin_snap, end_snap)
        return data
    
    async def ash_overall_wait(self, cus_code: str, dbid: int64, begin_snap: int32, end_snap: int32):
        query = """ SELECT DBID, INSTANCE_NUMBER, instance_name, DB_NAME , pdb_name, PCT FROM (SELECT DBID, INSTANCE_NUMBER, instance_name, caoi.DB_NAME , pdb_name, ROUND(SUM(time_waited) * 100 / nullif(SUM(SUM(time_waited))     OVER (partition by DBID, INSTANCE_NUMBER),0), 2)   PCT FROM CDB_ASH_OVERALL_ITEMS caoi WHERE CUS_CODE = :P_CUS_CODE  AND caoi.DBID = :P_DBID AND caoi.SNAP_ID BETWEEN :P_BEGIN_SNAP AND :P_END_SNAP GROUP BY instance_name, caoi.DB_NAME , pdb_name, DBID, INSTANCE_NUMBER) a WHERE a.PCT > 1 ORDER BY instance_name, pct DESC
            """
        data = await self.get_data(query, AshOverallWait, cus_code, dbid, begin_snap, end_snap)
        return data
    
    async def ash_overall_wait_global(self, cus_code: str, dbid: int64, begin_snap: int32, end_snap: int32):
        query = """ SELECT DBID, INSTANCE_NUMBER, instance_name, DB_NAME , pdb_name, avg(PCT) PCT FROM (SELECT DBID, INSTANCE_NUMBER, instance_name, caoi.DB_NAME , pdb_name, ROUND(SUM(time_waited) * 100 / nullif(SUM(SUM(time_waited)) OVER (partition by DBID, INSTANCE_NUMBER),0), 2) PCT FROM CDB_ASH_OVERALL_ITEMS caoi WHERE CUS_CODE = :P_CUS_CODE  AND caoi.DBID = :P_DBID AND caoi.SNAP_ID BETWEEN :P_BEGIN_SNAP AND :P_END_SNAP GROUP BY instance_name, caoi.DB_NAME , pdb_name, caoi.sql_id, DBID, INSTANCE_NUMBER) a GROUP BY DBID, INSTANCE_NUMBER, instance_name, DB_NAME , pdb_name ORDER BY pct DESC
            """
        data = await self.get_data(query, AshOverallWait, cus_code, dbid, begin_snap, end_snap)
        return data






    
    #     # return self.getValue(CdbEnum.DBINFO, DbInfo, 
    #     #                     dbid, begin_snap, end_snap)
    
    # #  = 'cdb.best_practice_19c'
    # # def getSqlPlanChange(self, dbid:int64, begin_snap: int32, end_snap: int32):
    # #     return self.getValue(CdbEnum.BEST_PRACTICE_19C, AshOverallWaitGlobal, 
    # #                         dbid, begin_snap, end_snap)

    # def getDbInfo(self, dbid:int64):
    #      return super().getDbInfo(CdbEnum.DB_INFO.value, dbid)
            
    # def getExtractTopSqlCpu(self, top_n_rows:int = 10):
    #     return self.extractTopSql(CdbEnum.EXTRACT_TOP_SQL_CPU, top_n_rows)

    # def getExtractTopSqlWait(self, top_n_rows:int = 10):
    #     return self.extractTopSql(CdbEnum.EXTRACT_TOP_SQL_WAIT, top_n_rows)

    # def getExtractTopSqlIo(self, top_n_rows:int = 10):
    #     return self.extractTopSql(CdbEnum.EXTRACT_TOP_SQL_IO, top_n_rows)
