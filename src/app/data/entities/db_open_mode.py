from base.domain.base_entity import BaseEntity

class DbOpenMode(BaseEntity):
        
    OpenMode : str
    
    key_map = {        
        "OPEN_MODE"   : "OpenMode"
    }  
    
    def __init__(self, **kwargs):
        """
        DbOpenMode model, inheriting from BaseModel.
        
        :param **kwargs: The kwagrs for DbOpenMode
        """
        super().__init__(**kwargs)
    