# 

from app.data.models.cdb.ash_base import CdbBaseEntity


class AshOverallEvent(CdbBaseEntity):

    Event: str
    Percentage: float
    
    key_map = {
        **CdbBaseEntity.key_map,
        "EVENT": "Event",
        "PCT": "Percentage"
    }
    
