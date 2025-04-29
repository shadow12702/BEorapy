# Description: DbContextConfigRequest

from pydantic import BaseModel

class DbContextConfigRequest(BaseModel):
    min_pool_size: int
    max_pool_size: int
    increment: int
    username: str
    password: str
    dsn: str
