# 

from datetime import datetime

from numpy import int32, int64
from base.model.mapped_base_model import MappedBaseModel

class AwrRepoInfoModel(MappedBaseModel):
    
    CustomerCode: str
    CustomerName: str
    Version: str
    DbName: str
    Cdb: bool = False
    CdbDbid: int64
    PdbDbid: int64
    PdbName: str
    BeginSnap: int32
    BeginTime: datetime
    EndSnap: int32
    EndTime: datetime
    
    key_map = {
        "CUS_CODE" : "CustomerCode",
        "CUS_NAME" : "CustomerName",
        "VERSION" : "Version",
        "DB_NAME"   : "DbName",
        "CDB"       : "Cdb",
        "CDB_DBID" : "CdbDbid",
        "PDB_DBID" : "PdbDbid",
        "PDB_NAME" : "PdbName",
        "BEGIN_SNAP" : "BeginSnap",
        "BEGIN_TIME" : "BeginTime",
        "END_SNAP" : "EndSnap",
        "END_TIME" : "EndTime"
    }

