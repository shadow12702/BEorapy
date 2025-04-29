from fastapi import APIRouter, Depends
from dependencies import get_admin_factory, AdminFactory
from app.services.auth_service import AccountService
from admin.models.request_model import RegisterRequest
from admin.presentation.controller import AccountController
from app.models.response_model import successful, failed

account_route = APIRouter(tags=["Account"])

def get_account_controller(admin_factory: AdminFactory = Depends(get_admin_factory)):
    return AccountController(AccountService(admin_factory))

@account_route.post('/register', response_model=None)
async def register_account(request: RegisterRequest,
                           account_controller: AccountController = Depends(get_account_controller)):
    try:
        await account_controller.register(request)
        return successful
    except Exception as ex:
        return failed(ex)