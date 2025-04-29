# 

from app.data.models.cdb.ash_base import CdbBaseEntity


class AshOverallWait(CdbBaseEntity):

    Percentage: float
    
    key_map = {
        **CdbBaseEntity.key_map,
        "PCT": "Percentage"
    }
    
