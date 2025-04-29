# 

from app.data.models.cdb.ash_base import CdbBaseEntity


class AshOverallModule(CdbBaseEntity):

    Module: str
    Percentage: float
    
    key_map = {
        **CdbBaseEntity.key_map,
        "MODULE": "Module",
        "PCT": "Percentage"
    }
    
