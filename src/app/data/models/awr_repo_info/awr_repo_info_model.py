# 

from datetime import datetime
from numpy import int32, int64
from base.domain.base_entity import BaseEntity

class AwrRepoInfoModel(BaseEntity):
    
    customer_code: str
    customer_name: str
    version: str
    database_name: str
    is_cdb: bool = False
    dbid: int64
    pdb_dbid: int64
    pdb_name: str
    begin_snap: int32
    begin_time: datetime
    end_snap: int32
    end_time: datetime
    is_rac: int
    is_exa: int
    block_size: int

    key_map = {
        "CUS_CODE" : "customer_code",
        "CUS_NAME" : "customer_name",
        "VERSION" : "version",
        "CDB"       : "is_cdb",
        "DBID" : "dbid",
        "DB_NAME"   : "database_name",
        "PDB_DBID" : "pdb_dbid",
        "PDB_NAME" : "pdb_name",
        "BEGIN_SNAP" : "begin_snap",
        "BEGIN_TIME" : "begin_time",
        "END_SNAP" : "end_snap",
        "END_TIME" : "end_time",
        "RAC" : "is_rac",
        "EXA" : "is_exa",
        "BLOCK_SIZE" : "block_size"
    }

