from numpy import int64
from app.models.response_model import AwrRepoInfoResponse, AwrInfoCustomerResponse
from app.factory import ApplicationFactory
from logger import AppLogger

class AwrRepoInfoService():
    _logger = AppLogger().get_logger()
    
    def __init__(self , app_factory: ApplicationFactory ):
        try:
            self.respository = app_factory.awr_repo_info_repository()
        except Exception as ex:
            self._logger.error(f"get AwrRepoInfoService error : {ex}")
            raise ex

    async def get_awr_repo_info(self):
        try:
            awr_info = await self.respository.get_awr_repo_info()
            result = [
                AwrRepoInfoResponse.from_model(item)
                for item in awr_info
            ]
            return result
        except Exception as ex:
            self._logger.error(f"get get_awr_repo_info error : {ex}")
            raise ex
            
    async def get_awr_info_by_customer(self, customer_code: str):
        try:
            awr_info = await self.respository.get_awr_repo_by_customer_code(customer_code)
            result = [
                AwrInfoCustomerResponse.from_model(item)
                for item in awr_info
            ]
            return result
        except Exception as ex:
            self._logger.error(f"get get_awr_info_by_customer error : {ex}")
            raise ex
    
    async def get_awr_info_by_customer_and_dbid(self,customer_code: str, dbid: int64):
        try:
            awr_info = await self.respository.get_awr_info_by_customer_code_and_dbid(customer_code, dbid)
            
        except Exception as ex:
            self._logger.error(f"get awr_info_by_customer_and_dbid error: f{ex}")
            raise ex