# Description: ResponseModel

from base.base_response import BaseResponse, successful, failed
from admin.models.responses.menu_response import MenuResponse
from admin.models.responses.customers_response import CustomerResponse
from admin.models.responses.patch_response import PatchResponse
from admin.models.responses.best_practice_reponse import BestPracticeResponse
from admin.models.responses.config_response import ConfigResponse

__all__ = [
    "BaseResponse", 
    "successful",
    "failed",
    "MenuResponse",
    "CustomerResponse",
    "PatchResponse",
    "BestPracticeResponse",
    "ConfigResponse",
    
]