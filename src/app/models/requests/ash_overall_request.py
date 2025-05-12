# Description: AshOverallRequest

from pydantic import BaseModel

class AshOverallRequest(BaseModel):
    metric_type: str
    customer_code: str
    dbid: int
    begin_snap: int = 0
    end_snap: int = 0
    
