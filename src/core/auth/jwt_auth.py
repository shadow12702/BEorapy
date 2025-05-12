import asyncio
from datetime import datetime, timedelta
from jose import jwt, JWTError
from fastapi import HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
from dependencies import config_manager as cf_manager

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='/auth/login')

class JwtAuth:
    
    @staticmethod
    async def generate_token(data: dict, token_type: str = "access"):
        def sync_gen_token(token_type: str):
            if token_type not in ["access", "refresh"]:
                raise ValueError("Token type must be either 'access' or 'refresh'")
            if not isinstance(data, dict):
                raise ValueError("Token data must be a dictionary")
            try:
                jwt_auth = cf_manager.jwt_auth_config
                to_encode = data.copy()
                expire = datetime.utcnow() +  (timedelta(minutes=jwt_auth.TokenExpireMinutes) if token_type == "access" else timedelta(days=jwt_auth.RefreshExpireDays))
                to_encode.update({'exp' : expire})
                return jwt.encode(to_encode, jwt_auth.JwtAuthKey, algorithm=jwt_auth.Algorithm)
            except (TypeError, ValueError) as ex:
                raise HTTPException(status_code=401, detail=f"Invalid token data: {ex}")
            except JWTError as ex:
                raise HTTPException(status_code=401, detail=f"JWT error: {ex}")
            except Exception as ex:
                raise HTTPException(status_code=401, detail=ex)
        return await asyncio.to_thread(sync_gen_token, token_type)
        
    @staticmethod
    async def decode_token(token: str):
        def sync_decode_token():
            try:
                jwt_auth = cf_manager.jwt_auth_config
                payload = jwt.decode(token, jwt_auth.JwtAuthKey, algorithms=[jwt_auth.Algorithm])
                username: str = payload.get("username")
                if username is None:
                    raise HTTPException(status_code=401, detail="Invalid token")
                return payload
            except JWTError as ex:
                raise HTTPException(status_code=401, detail=ex)
        return await asyncio.to_thread(sync_decode_token)
        
    @staticmethod
    async def get_current_user(token: str = Depends(oauth2_scheme)):
        return await JwtAuth.decode_token(token)
    
    @staticmethod
    async def verify_token(token: str):
        def sync_verify_token():
            try:
                jwt_auth = cf_manager.jwt_auth_config
                payload = jwt.decode(token, jwt_auth.JwtAuthKey, algorithms=[jwt_auth.Algorithm])
                return payload
            except JWTError as ex:
                raise ex
        return await asyncio.to_thread(sync_verify_token)
