# Description: JwtAuthConfigRequest

from pydantic import BaseModel

class JwtAuthConfigRequest(BaseModel):
    token_expire_minutes: int
    refresh_expire_days: int
    