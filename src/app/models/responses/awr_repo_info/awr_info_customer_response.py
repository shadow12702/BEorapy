# 

from pydantic import BaseModel

class AwrInfoCustomerResponse(BaseModel):
    dbid: int
    db_name: str