from fastapi.responses import JSONResponse
from pydantic import BaseModel
from enum import Enum

class ResponseCode(Enum):
    OK = "OK"
    FAILED = "FAILED"

class BaseResponse(BaseModel):
    code: ResponseCode
    message: str
       
def successful(detail: str = "Successfully"):
    resp = BaseResponse(**{
        'code': ResponseCode.OK, 
        'message': detail
    })
    return JSONResponse(status_code=200, content=resp)

def failed(detail):
    resp = BaseResponse(**{
        'code': ResponseCode.FAILED, 
        'message': detail
    })
    return JSONResponse(status_code=400, content=resp)
