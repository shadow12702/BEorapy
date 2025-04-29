from base.domain.base_entity import BaseEntity

class CheckDb(BaseEntity):
   
        
    def __init__(self, **kwargs):
        """
        CheckDb status model, inheriting from BaseModel.
        
        :param id: Index of name.
        :param **kwargs: The kwagrs for checkdb.        
        """
        self.Name:str = None
        self.Value:str = None
        
        self.key_map.update({
            "NAME"   : "Name",
            "VALUE"  : "Value"
        })        
        super().__init__(**kwargs)
    
        
    