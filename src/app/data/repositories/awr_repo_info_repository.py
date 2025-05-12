# app/data/repositories/awr_repo_info_repository.py

from typing import List
from numpy import int64
from logger import AppLogger
from data.db_context import DbContext, DataOperators
from app.data.models.awr_repo_info.awr_repo_info_model import AwrRepoInfoModel


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
                    FROM VW_AWR_REPO_INFO ari
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
            query = """SELECT CUS_CODE, CASE WHEN CDB='YES' THEN PDB_DBID ELSE DBID END DBID, 
                            CASE WHEN CDB='YES' THEN PDB_NAME  ELSE DB_NAME END DB_NAME,
                            VERSION, CDB, BEGIN_SNAP, BEGIN_TIME, END_SNAP, END_TIME, RAC, EXA, BLOCK_SIZE
                        FROM VW_AWR_REPO_INFO
                        WHERE CUS_CODE = :V_CUS_CODE 
                        ORDER BY DBID"""
            awr_info = await self.db_context.get_data(query, { "V_CUS_CODE": customer_code })
            return [AwrRepoInfoModel(**a) for a in awr_info]
        except Exception as ex:
            self._logger.error(f"get awr repo info by customer code failed. {ex}")

    async def get_awr_info_by_customer_code_and_dbid(self, customer_code: str, dbid: int64):
        '''Get Awr Repo Info list depend on customer and dbid'''
        try:
            query = """SELECT * 
                        FROM VW_AWR_REPO_INFO
                        WHERE CUS_CODE = :V_CUS_CODE
                        AND CASE WHEN CDB = 'YES' THEN CDB_DBID ELSE PDB_DBID END = :V_DBID"""
            awr_info = await self.db_context.get_data(query, { 
                "V_CUS_CODE": customer_code , 
                "V_DBID": dbid
                })
            return [AwrRepoInfoModel(**a) for a in awr_info]
        except Exception as ex:
            self._logger.error(f"get awr repo info by customer code failed. {ex}")

    