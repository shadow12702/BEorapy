# 
    
from base.domain.base_entity import BaseEntity

class AshOverallObjectMetricModel(BaseEntity):

    InstanceName: str
    DbName: str
    PdbName: str
    Owner: str
    ObjectName: str
    Percentage: float

    key_map = {
        **BaseEntity.key_map,
        "INSTANCE_NAME" : "InstanceName",
        "DB_NAME": "DbName",
        "PDB_NAME" : "PdbName",
        "OWNER" : "Owner", 
        "OBJECT_NAME": "ObjectName", 
        "PERCENTAGE": "Percentage"
    }
