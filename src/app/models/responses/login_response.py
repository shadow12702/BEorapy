from datetime import datetime
from pydantic import BaseModel

class User(BaseModel):
    Username: str
    Email: str        
    IsAdmin: bool
    LastIpAddress: str
    LastLoginDate: datetime
    
class Token(BaseModel):
    access: str
    refresh: str

class LoginResponse(BaseModel):
    user: User
    token: Token
