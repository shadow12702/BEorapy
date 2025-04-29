# Description: MenuTypeRequest

from pydantic import BaseModel

class MenuTypeRequest(BaseModel):
    type: int = 0