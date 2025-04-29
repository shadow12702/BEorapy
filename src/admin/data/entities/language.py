# Description: Language

from base.domain.base_entity import BaseEntity

class Language(BaseEntity):
    Code         : str
    Name         : str
    Culture      : str
    FlagName     : str
    IsPublished  : int
    DisplayOrder : int
    
    key_map = {
        **BaseEntity.key_map,
        "CODE"           : "Code"         ,
        "LANG_NAME"      : "Name"         ,
        "LANG_CULTURE"   : "Culture"      ,
        "LANG_FLAG_NAME" : "FlagName"     ,
        "IS_PUBLISHED"   : "IsPublished"  ,
        "DISPLAY_ORDER"  : "DisplayOrder" 
    }
    