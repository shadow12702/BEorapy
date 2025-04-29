
import asyncio
from datetime import datetime

from core.auth.jwt_auth import JwtAuth
from dependencies import config_manager as cf_manager


class TokenManager:
    _instance = None
    
    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)
            cls._instance.tokens = set()
            asyncio.create_task(cls._instance._cleanup_expired_tokens())
        return cls._instance

    async def _cleanup_expired_tokens(self):
        '''clean token manager'''
        await asyncio.sleep(10) #Delay 10s for application started
        while True:
            token_manager_option = cf_manager.all_config.token_manager            
            try:
                clean_time = int(token_manager_option.clean_token_manager_time)*60
            except (AttributeError, ValueError):
                clean_time = 60

            await asyncio.sleep(clean_time)
            
            async def validate_token(token):
                try:
                    payload = await JwtAuth.verify_token(token)
                    exp = payload.get('exp')
                    if exp and datetime.utcnow() > datetime.utcfromtimestamp(exp):
                        return ''
                    return token
                except:
                    return ''
    
            self.tokens = {token for token in self.tokens if token == await validate_token(token)}

    def add_token(self, token):
        self.tokens.add(token)

token_manager = TokenManager()