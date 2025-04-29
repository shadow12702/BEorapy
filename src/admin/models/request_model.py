# Description: RequestModel

from admin.models.requests.config.app_config_request import AppConfigRequest
from admin.models.requests.config.db_context_config_request import DbContextConfigRequest
from admin.models.requests.config.jwt_auth_config_request import JwtAuthConfigRequest
from admin.models.requests.config.logging_config_request import LoggingConfigRequest
from admin.models.requests.config.mail_config_request import MailConfigRequest
from admin.models.requests.menu.menu_request import MenuRequest
from admin.models.requests.menu.menu_type_request import MenuTypeRequest
from admin.models.requests.register_request import RegisterRequest
from admin.models.requests.customer.customer_request import CustomerRequest 
from admin.models.requests.customer.update_customer_request import UpdateCustomerRequest
from admin.models.requests.patch.patch_request import PatchRequest
from admin.models.requests.patch.patch_update_request import PatchUpdateRequest
from admin.models.requests.best_practice.best_practice_request import BestPracticeRequest
from admin.models.requests.config.config_request import ConfigRequest

__all__ = [
    "AppConfigRequest",
    "DbContextConfigRequest",
    "JwtAuthConfigRequest",
    "LoggingConfigRequest",
    "MailConfigRequest",
    "MenuRequest",
    "MenuTypeRequest",
    "RegisterRequest",
    "CustomerRequest",
    "UpdateCustomerRequest",
    "PatchRequest",
    "PatchUpdateRequest",
    "BestPracticeRequest",
    "ConfigRequest",
]
