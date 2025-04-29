# 

from numpy import int64
from base.domain.base_entity import BaseEntity


class CdbBaseEntity(BaseEntity):

    Dbid: int64
    InstanceName: str
    DbName: str
    PdbName: str

    key_map = {
        "DBID" : "Dbid", 
        "INSTANCE_NAME": "InstanceName", 
        "DB_NAME": "DbName", 
        "PDB_NAME" : "PdbName"
    }