from datetime import datetime
from typing import Optional
from pydantic import BaseModel

class User(BaseModel):
    username: str
    email: Optional[str] = None
    is_admin: bool = False
    last_ip_address: str
    last_login_date: datetime = datetime.utcnow()
    
class Token(BaseModel):
    access: str
    refresh: str

class LoginResponse(BaseModel):
    user: User
    token: Token
