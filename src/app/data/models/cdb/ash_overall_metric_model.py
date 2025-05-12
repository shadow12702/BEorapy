# 

from base.domain.base_entity import BaseEntity

class AshOverallMetricModel(BaseEntity):

    InstanceName: str
    DbName: str
    PdbName: str
    MetricValue: str
    Percentage: float
    
    key_map = {
        **BaseEntity.key_map,
        "INSTANCE_NAME": "InstanceName", 
        "DB_NAME": "DbName", 
        "PDB_NAME" : "PdbName",
        "METRIC_VALUE": "MetricValue",
        "PERCENTAGE": "Percentage"
    }
    