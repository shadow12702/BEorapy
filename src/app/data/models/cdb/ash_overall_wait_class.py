# 

from app.data.models.cdb.ash_base import CdbBaseEntity


class AshOverallWaitClass(CdbBaseEntity):

    WaitClass: str
    Percentage: float
    
    key_map = {
        **CdbBaseEntity.key_map,
        "WAIT_CLASS": "WaitClass",
        "PCT": "Percentage"
    }
    
