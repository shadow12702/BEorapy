from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from datetime import datetime
from jose import JWTError
from core.auth.token_manager import token_manager
from dependencies import get_admin_factory, AdminFactory
from core.auth.jwt_auth import JwtAuth
from admin.services.account_service import AccountService
from app.services.auth_service import AuthService
from app.presentation.controller import AuthController
from app.models.request_model import LoginRequest, TokenRequest
from app.models.response_model import LoginResponse, RefreshTokenResponse, failed, successful


auth_route = APIRouter(tags=["Authentication"])
http_bearer = HTTPBearer()

def get_auth_controller(admin_factory: AdminFactory = Depends(get_admin_factory)):
    return AuthController(AuthService(AccountService(admin_factory)))

async def verify_auth(credential: HTTPAuthorizationCredentials = Depends(http_bearer)):
    if not credential:
        raise HTTPException(status_code=401, detail="Token is missing")
    try:
        token = credential.credentials
        if token in token_manager.tokens:
            raise HTTPException(status_code=401, detail="Token is invalid")
        payload = await JwtAuth.verify_token(token)
        exp = payload.get("exp")
        if exp and datetime.utcnow() > datetime.utcfromtimestamp(exp):
            raise HTTPException(status_code=401, detail="Token expired")
        return payload
    except JWTError:
        raise HTTPException(status_code=403, detail="Invalid token")


@auth_route.post('/login', response_model=LoginResponse)
async def login(login: LoginRequest, 
                auth_controller: AuthController = Depends(get_auth_controller)):
    try:
        user = await auth_controller.login(login)   
        return LoginResponse(**user)
    except Exception as ex:
        return failed("Login failed")

@auth_route.post('/logout', response_model= None)
async def logout(token: TokenRequest, auth_controller: AuthController = Depends(get_auth_controller)):
    try: 
        await auth_controller.logout(token)
        return successful
    except Exception as ex:
        return failed(ex)

@auth_route.post('/verify_token', response_model=None)
async def verify_token(token:TokenRequest):
    try:
        _token = token.model_dump()
        payload = await JwtAuth.verify_token(_token.get('token',{}))
        exp = payload.get('exp')
        if exp and datetime.utcnow() > datetime.utcfromtimestamp(exp):
            raise HTTPException(status_code=401, detail="Token expired")
        return True
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")

    
@auth_route.post('/refresh-token', response_model=RefreshTokenResponse)
async def refresh_token(token: TokenRequest, 
                        auth_controller: AuthController = Depends(get_auth_controller)):
    try:
        token = await auth_controller.refresh_token(token)
        return RefreshTokenResponse(**token)
    except Exception as ex:
        return failed(ex)