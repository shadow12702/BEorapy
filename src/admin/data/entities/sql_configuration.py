from base.domain.base_entity import BaseEntity

class SqlConfiguration(BaseEntity):
    
    Code: str
    Value: str
    Idx: int
    IsUsed: int
    
    key_map = {
        **BaseEntity.key_map,
        "CF_CODE"      : "Code" ,
        "CF_VALUE"     : "Value",
        "CF_IDX"       : "Idx", 
        "CF_IS_USED"   : "IsUsed"
    }
    