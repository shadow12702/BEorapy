from fastapi import HTTPException
from admin.services.account_service import AccountService
from admin.models.request_model import RegisterRequest
from helper import helper

class AccountController:
    
    def __init__(self, account_service: AccountService):
        self.accountService = account_service
    
    
    async def register(self, register_request: RegisterRequest):
        try:
            request = register_request.model_dump()
            username = request.get("username", None)
            password = request.get("password", None)
            email = request.get("email", None)
            
            if not helper.strNotEmpty(username):
                raise HTTPException(status_code=400, detail="Invalid username")
            if not helper.strNotEmpty(password):
                raise HTTPException(status_code=400, detail="Invalid password")
            if not helper.emailValid(email):
                raise HTTPException(status_code=400, detail="Invalid email")
            
            if not helper.strNotEmpty(email):
                return await self.accountService.register(username, password)
            else:
                return await self.accountService.register(username, password, email)                
            
        except Exception as ex:
            raise HTTPException(status_code=400, detail=f"{ex}")
    
