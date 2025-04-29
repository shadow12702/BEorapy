from pydantic import BaseModel

class MenuResponse(BaseModel):
    code: str
    name: str
    icon: str = ''
    parent: str = ''
    route: str = ''
    is_show: bool = False
    