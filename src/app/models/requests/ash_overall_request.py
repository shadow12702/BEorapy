# Description: AshOverallRequest

from pydantic import BaseModel

class AshOverallRequest(BaseModel):
    customer_code: str
    dbid: int

