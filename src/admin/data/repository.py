# Description: Repository

from admin.data.repositories.account_repository import AccountRepository
from admin.data.repositories.config_repository import ConfigRepository
from admin.data.repositories.language_repository import LanguageRepository
from admin.data.repositories.menu_repository import MenuRepository
from admin.data.repositories.sql_configuration_repository import SqlConfigurationRepository
from admin.data.repositories.customer_repository import CustomerRepository

from admin.data.repositories.patch_repository import PatchRepository
from admin.data.repositories.best_practice_repository import BestPracticeRepository

__all__ = [
    "AccountRepository",
    "ConfigRepository",
    "LanguageRepository",
    "MenuRepository",
    "SqlConfigurationRepository",
    "CustomerRepository",
    "PatchRepository",
    "BestPracticeRepository",
    
]

