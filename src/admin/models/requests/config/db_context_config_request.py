# Description: DbContextConfigRequest

from pydantic import BaseModel

class DbContextConfigRequest(BaseModel):
    min_pool_size: int = 2
    max_pool_size: int = 10
    increment: int = 1
    username: str = "username"
    password: str = "password"
    dsn: str = "dsn"
