from pydantic import BaseModel

class AwrCustomerDbidRequest(BaseModel):
    customer_code:str
    dbid: int