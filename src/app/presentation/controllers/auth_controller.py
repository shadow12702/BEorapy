from fastapi import HTTPException
from app.services.auth_service import AuthService
from app.models.request_model import LoginRequest, TokenRequest

class AuthController:
    
    def __init__(self, auth_service: AuthService):
        self._service = auth_service
        
    async def login(self, login_request: LoginRequest):
        '''Login system'''
        try:
            user =  await self._service.login(login_request.username, 
                                   login_request.password, 
                                   login_request.ip_address
                                   )
            return user
        except Exception as ex:
            raise HTTPException(status_code=401, detail=f"Invalid credentials {ex}")
    
    async def logout(self, token_request: TokenRequest):
        try:
            await self._service.logout(token_request.token)
        except:
            raise HTTPException(status_code=401, detail="Token invalid")
    
    async def refresh_token(self, token_request: TokenRequest):
        '''Refresh token'''
        try:
            return await self._service.refresh_token(token_request.token)
        except:
            raise HTTPException(status_code=401, detail="Invalid refresh token")
