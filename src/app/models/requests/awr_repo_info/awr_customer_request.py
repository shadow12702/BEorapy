# 
from pydantic import BaseModel

class AwrCustomerRequest(BaseModel):
    customer_code:str
 