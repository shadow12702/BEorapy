from pydantic import BaseModel

class MenuResponse(BaseModel):
    code: str
    name: str
    icon: str = ''
    parent: str = ''
    prefix: str = ''
    route: str = ''
    is_show: bool = False
    
    @classmethod
    def from_model(cls, model):
        return cls(
            code = model.code,
            name = model.name,
            icon = model.icon if model.icon else '',
            parent = model.parent if model.parent else '',
            prefix = model.prefix if model.prefix else '',
            route = model.route if model.route else '',
            is_show = model.is_show == 1
        )
    