# Description: LoginRequest

from pydantic import BaseModel

class LoginRequest(BaseModel):
    username: str
    password: str
    ip_address: str
