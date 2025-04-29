# Description: 

import asyncio
from admin.services.account_service import AccountService
from core.auth.jwt_auth import JwtAuth
from core.auth.token_manager import token_manager
from logger import AppLogger

class AuthService:
    _logger = AppLogger().get_logger()
    
    def __init__(self, account_service: AccountService):
        self.accountService = account_service
        self.token_backlist = set()
        
    async def login(self, username: str, password: str, ip_address: str):
        '''Login to system
        
        Params:
            username : username login to system
            password : password of user
            ip_address : IP address of machine that use to login 
        Returns:
            access_token, refresh_token : access token and refresh token'''
        try:
            user = await self.accountService.login(username, password, ip_address)
            if user.is_empty:
               raise "Login failed" 
            info = {"username": user.Username, 
                    "email": user.Email, 
                    "is_admin": user.IsAdmin,
                    "last_ip_address": user.LastIpAddress, 
                    "last_login_date":user.LastLoginDate.isoformat()
                }
            access_token = await JwtAuth.create_token(info)
            refresh_token = await JwtAuth.refresh_token(info)
            return {"token": {"access": access_token, "refresh": refresh_token},
                    "user": user.to_dict()
                    }
            
        except Exception as ex:
            self._logger.error(f"Login failed {ex}")
        
    async def logout(self, token:str):
        def sync_logout():
            try:
                return token_manager.add_token(token)
            except Exception as ex:
                self._logger.error("Loged out failed")
                
        return await asyncio.to_thread(sync_logout)
    
    async def refresh_token(self, refresh_token:str):
        '''Refresh token to keep loging into system
        
        Params:
            refresh_token: refresh token of current user
            
        Returns:
            return new access token'''
        try:
            user = await JwtAuth.decode_token(refresh_token)
            if refresh_token in token_manager.tokens:
                raise Exception({"status":401, "message": "Refresh token is invalid"})
            info = {"username": user.get("username"), 
                    "email": user.get("email"), 
                    "is_admin": user.get("is_admin"),
                    "last_ip_address": user.get("last_ip_address"), 
                    "last_login_date":user.get("last_login_date")
                }
            access_token = await JwtAuth.create_token(info)
            return {"token": access_token}
        except Exception as ex:
            self._logger.error(f"Refresh token error {ex}")
            
    
    async def current_user(self, token: str):
        '''Get current user by decoding token
        
        Params:
            token: token of current user is loging to system
        '''
        try:
            username = await JwtAuth.decode_token(token)
            return await self.accountService.get_account(username)
        except Exception as ex:
            self._logger.error(f"getcurrent")
    
        