# Description: Route

from admin.presentation.routes.account_route import account_route
from admin.presentation.routes.config_route import config_router
from admin.presentation.routes.menu_route import menu_router
from admin.presentation.routes.customer_route import customer_router

from admin.presentation.routes.patch_route import patch_router
from admin.presentation.routes.best_practice_route import best_practice_router

__all__ = [
    "account_route",
    "config_router", 
    "menu_router",
    "customer_router",
    "patch_router",
    "best_practice_router",
    
]

