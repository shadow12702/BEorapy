from fastapi import HTTPException
from app.models.requests.awr_repo_info.awr_customer_request import AwrCustomerRequest
from app.services.awr_repo_info_service import AwrRepoInfoService
from helper import helper

class AwrRepoInfoController:
    def __init__(self , awr_service: AwrRepoInfoService):
        self.service = awr_service
    
    async def get_awr_repo_info(self):
        '''Get all awr'''
        try:
            awr_info = await self.service.get_awr_repo_info()
            return awr_info
        except Exception as ex:
            raise HTTPException(status_code=400, detail=f"{ex}")
    
    async def get_awr_repo_by_customer(self, request: AwrCustomerRequest):
        try:
            if not helper.strNotEmpty(request.customer_code):
                raise HTTPException(status_code=400, detail="Customer code is required")
            return await self.service.get_awr_info_by_customer(request.customer_code)
        except Exception as ex:
            raise HTTPException(status_code=400, detail=f"{ex}")