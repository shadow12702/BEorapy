from pydantic import BaseModel

class MenuRequest(BaseModel):
    name: str
    icon: str
    parent: str
    route: str
    is_show: bool = True    
    