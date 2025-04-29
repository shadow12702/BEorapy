# Description: TokenRequest

from pydantic import BaseModel

class TokenRequest(BaseModel):
    token: str