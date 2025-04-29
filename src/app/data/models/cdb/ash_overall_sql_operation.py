# 

from app.data.models.cdb.ash_base import CdbBaseEntity


class AshOverallSqlOperation(CdbBaseEntity):

    Operation: str
    Percentage: float
    
    key_map = {
        **CdbBaseEntity.key_map,
        "OPERATION": "Operation",
        "PCT": "Percentage"
    }
    
