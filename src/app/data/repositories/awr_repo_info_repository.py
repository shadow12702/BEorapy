from typing import List

from numpy import int64
from app.data.models.awr_repo_info.awr_info_customer_model import AwrInfoCustomerModel
from app.data.models.awr_repo_info.awr_repo_info_model import AwrRepoInfoModel
from app.data.models.awr_repo_info.awr_repo_process_model import AwrRepoProcessModel
from logger import AppLogger
from data.db_context import DbContext, DataOperators

class AwrRepoInfoRepository():
    _logger = AppLogger().get_logger()
    
    def __init__(self, db_context: DbContext):
        if not isinstance(db_context, DataOperators):
            self._logger.error("db_context must be a part of DataOperators")
            raise TypeError("db_context must be a part of DataOperators")
        self.db_context = db_context
        
        
    async def get_awr_repo_info(self) -> List[AwrRepoInfoModel]:
        '''Get all awr repo info'''
        try:
            query = """SELECT  ari.*, 
                        c.CUS_NAME
                    FROM AWR_REPO_INFO ari
                        INNER JOIN Customer c ON ari.CUS_CODE = c.CUS_CODE
                    ORDER BY  ari.CUS_CODE, ari.DB_NAME
                    """            
            awr_repo_info = await self.db_context.get_data(query)      
            return [AwrRepoInfoModel(**a) for a in awr_repo_info ]
        
        except Exception as ex:
            self._logger.error(f"get AwrRepoInfo error {ex}")

    async def get_awr_repo_by_customer_code(self, customer_code: str):
        '''Get Awr Repo Info list depend on customer'''
        try:
            query = """SELECT CASE WHEN CDB=1 THEN CDB_DBID ELSE PDB_DBID END DBID, 
                    DB_NAME 
                FROM AWR_REPO_INFO
                WHERE CUS_CODE = :V_CUS_CODE
                ORDER BY DBID"""
            awr_info = await self.db_context.get_data(query, { "V_CUS_CODE": customer_code })
            return [AwrInfoCustomerModel(**a) for a in awr_info]
        except Exception as ex:
            self._logger.error(f"get awr repo info by customer code failed. {ex}")

    async def get_awr_info_by_customer_code_and_dbid(self, customer_code: str, dbid: int64):
        '''Get Awr Repo Info list depend on customer and dbid'''
        try:
            query = """SELECT * 
                        FROM AWR_REPO_INFO
                        WHERE CUS_CODE = :V_CUS_CODE
                        AND CASE WHEN CDB = 1 THEN CDB_DBID ELSE PDB_DBID END = :V_DBID"""
            awr_info = await self.db_context.get_data(query, { 
                "V_CUS_CODE": customer_code , 
                "V_DBID": dbid
                })
            return [AwrRepoProcessModel(**a) for a in awr_info]
        except Exception as ex:
            self._logger.error(f"get awr repo info by customer code failed. {ex}")

    