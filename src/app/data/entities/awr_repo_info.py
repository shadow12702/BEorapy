from datetime import datetime
from typing import Optional
from base.model.mapped_base_model import MappedBaseModel

class AwrRepoInfoModel(MappedBaseModel):
    CustomerCode: str
    CustomerName: str
    Version: str
    DbName: str
    Cdb: bool = False
    CdbDbid: int
    PdbDbid: int
    PdbName: str
    EndSnap: Optional[int] = None
    EndTime: Optional[datetime] = None

    key_map = {
        "CUS_CODE"    : "CustomerCode",
        "CUS_NAME"    : "CustomerName",
        "VERSION"     : "Version",
        "DB_NAME"     : "DbName",
        "CDB"         : "Cdb",
        "CDB_DBID"    : "CdbDbid",
        "PDB_DBID"    : "PdbDbid",
        "PDB_NAME"    : "PdbName",
        "END_SNAP"    : "EndSnap",
        "END_TIME"    : "EndTime"
    }
