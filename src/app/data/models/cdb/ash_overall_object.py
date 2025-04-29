# DBID, A.INSTANCE_NAME , DB_NAME, A.PDB_NAME , OWNER, OBJECT_NAME, A.PCT 
    
from app.data.models.cdb.ash_base import CdbBaseEntity

class AshOverallObject(CdbBaseEntity):

    
    Owner: str
    ObjectName: str
    Percentage: float

    key_map = {
        **CdbBaseEntity.key_map,
        "OWNER" : "Owner", 
        "OBJECT_NAME": "ObjectName", 
        "PCT": "Percentage"
    }

    