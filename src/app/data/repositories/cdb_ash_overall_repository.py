from numpy import int32, int64
from data.db_context import DbContext, DataOperators
from app.data.repositories.general_repository import GeneralRepository
from logger import AppLogger
from app.data.models.cdb_model import *

    
class CdbAshOverallRepository(GeneralRepository):
    
    _logger = AppLogger().get_logger()
    
    def __init__(self, db_context: DbContext):
        
        if not isinstance(db_context, DataOperators):
            self._logger.error(TypeError("db_context must implement DataOperations"))        
        self.db_context = db_context
    
    async def ash_overall_metric(self, metric_type:str, customer_code: str, dbid: int64, begin_snap: int32, end_snap: int32):
        try:
            proc_name = "CDB_RPT_PKG.ASH_OVERALL_METRIC"
            data = await self.db_context.call_procedure(proc_name, 
                                                 input_params= {
                                                     "P_CUS_CODE" : customer_code,
                                                     "P_METRIC_TYPE": metric_type, 
                                                     "P_DBID" : dbid,
                                                     "P_BEGIN_SNAP" : begin_snap,
                                                     "P_END_SNAP" : end_snap 
                                                     },
                                                 output_cursor=True)
            return [AshOverallMetricModel(**item) for item in data]
        except Exception as ex:
            self._logger.error(f"get ash_overall_metric failed!. Error: {ex}")

    async def ash_overall_object_metric(self, metric_type:str, customer_code: str, dbid: int64, begin_snap: int32, end_snap: int32):
        try:
            proc_name = "CDB_RPT_PKG.ASH_OVERALL_OBJECT_METRIC"
            data = await self.db_context.call_procedure(proc_name, 
                                                 input_params= {
                                                     "P_CUS_CODE" : customer_code,
                                                     "P_METRIC_TYPE": metric_type, 
                                                     "P_DBID" : dbid,
                                                     "P_BEGIN_SNAP" : begin_snap,
                                                     "P_END_SNAP" : end_snap 
                                                     },
                                                 output_cursor=True)
            
            return [AshOverallObjectMetricModel(**item) for item in data]
        except Exception as ex:
            self._logger.error(f"get ash_overall_object_metric failed!. Error: {ex}")


    
    # async def ash_overall_segment(self, cus_code: str, dbid: int64, begin_snap: int32, end_snap: int32):
    #     query = """SELECT DBID, A.INSTANCE_NAME , DB_NAME, A.PDB_NAME , OWNER, OBJECT_NAME, A.PCT 
    #     FROM (SELECT A.DBID, A.INSTANCE_NAME, A.DB_NAME , A.PDB_NAME , A.OWNER , A.OBJECT_NAME, 
    #             ROUND(SUM(TIME_WAITED) * 100 / NULLIF(SUM(SUM(TIME_WAITED)) OVER (PARTITION BY A.DBID, A.INSTANCE_NUMBER),0), 2) PCT 
    #         FROM CDB_ASH_OVERALL_OBJECTS A 
    #         WHERE CUS_CODE = :P_CUS_CODE 
    #             AND A.DBID = :P_DBID AND A.SNAP_ID BETWEEN :P_BEGIN_SNAP AND :P_END_SNAP  
    #         GROUP BY  A.DBID, A.INSTANCE_NAME, A.DB_NAME , A.PDB_NAME , A.OWNER , A.OBJECT_NAME ,A.INSTANCE_NUMBER ) A 
    #     WHERE A.PCT  > 1 
    #     ORDER BY DB_NAME,INSTANCE_NAME,PCT DESC, OBJECT_NAME"""
    #     data = await self.get_data(query, AshOverallObject, cus_code, dbid, begin_snap, end_snap)
    #     return data
    

    # async def ash_overall_sql_cpu(self, cus_code: str, dbid: int64, begin_snap: int32, end_snap: int32):
    #     query = """select a.cus_code, a.dbid, a.instance_number, instance_name, db_name, pdb_name, sql_id, pct  
    #         from ( select cus_code, dbid, instance_number,instance_name, db_name, pdb_name, sql_id, 
    #                     ROUND((RATIO_TO_REPORT(COUNT(*)) OVER (PARTITION BY A.DBID,A.INSTANCE_NUMBER))*100,2) PCT 
    #                 from cdb_ash_overall_items a 
    #                 where cus_code = :P_CUS_CODE  and a.dbid = :P_DBID and a.snap_id between :P_BEGIN_SNAP and :P_END_SNAP group by cus_code, dbid,instance_number,instance_name, db_name, cus_code,  pdb_name, sql_id ) a 
    #         where pct>1 order by instance_name, pct DESC"""
    #     data = await self.get_data(query, AshOverallSql, cus_code, dbid, begin_snap, end_snap)
    #     return data
    




    
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
