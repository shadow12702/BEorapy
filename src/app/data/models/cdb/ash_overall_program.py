# 

from app.data.models.cdb.ash_base import CdbBaseEntity


class AshOverallProgram(CdbBaseEntity):

    Program: str
    Percentage: float
    
    key_map = {
        **CdbBaseEntity.key_map,
        "PROGRAM": "Program",
        "PCT": "Percentage"
    }
    
