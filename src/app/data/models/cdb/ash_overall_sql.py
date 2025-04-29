# 

from app.data.models.cdb.ash_base import CdbBaseEntity


class AshOverallSql(CdbBaseEntity):

    SqlId: str
    Percentage: float
    
    key_map = {
        **CdbBaseEntity.key_map,
        "SQL_ID": "SqlId",
        "PCT": "Percentage"
    }
    
