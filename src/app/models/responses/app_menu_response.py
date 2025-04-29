from pydantic import BaseModel

class AppMenuResponse(BaseModel):
    name: str
    icon: str
    parent: str
    route: str
    is_show: bool
    