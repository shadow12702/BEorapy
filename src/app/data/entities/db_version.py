
from base.domain.base_entity import BaseEntity

class DbVersion(BaseEntity):
        
    Version : int 
    
    key_map = {        
        "VERSION"   : "Version"
    }  
    
    def __init__(self, **kwargs):
        """
        DbVersion model, inheriting from BaseModel.
        
        :param **kwargs: The kwagrs for DbVersion
        """
        super().__init__(**kwargs)
    
        