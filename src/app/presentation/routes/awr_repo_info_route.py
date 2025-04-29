from fastapi import APIRouter, Depends
from app.models.requests.awr_repo_info.awr_customer_request import AwrCustomerRequest
from app.presentation.route import verify_auth
from app.factory import ApplicationFactory
from dependencies import get_app_factory
from app.presentation.controller import AwrRepoInfoController
from app.services.awr_repo_info_service import AwrRepoInfoService
from app.models.response_model import successful, failed

awr_repo_info_router = APIRouter(tags=["Awr Repo Info"])

def get_awr_repo_info_controller(app_factory: ApplicationFactory = Depends(get_app_factory)):
    '''Get customer controller'''
    return AwrRepoInfoController(AwrRepoInfoService(app_factory))

@awr_repo_info_router.post("/get-awr-repo-info", response_model=None)
async def get_awr_repo_info(controller: AwrRepoInfoController = Depends(get_awr_repo_info_controller)):
    '''Get Awr by request'''
    try:
        return await controller.get_awr_repo_info()  
    except Exception as ex:
        return failed(f"{ex}")
    

@awr_repo_info_router.post("/get-awr-repo-by-customer", response_model=None)
async def get_awr_repo_by_customer(request: AwrCustomerRequest, controller: AwrRepoInfoController = Depends(get_awr_repo_info_controller)):
    '''Get Awr by request'''
    try:
        return await controller.get_awr_repo_by_customer(request)  
    except Exception as ex:
        return failed(f"{ex}")
    
    
    
