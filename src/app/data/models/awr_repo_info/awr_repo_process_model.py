# 


from datetime import datetime
from numpy import int32, int64
from base.model.mapped_base_model import MappedBaseModel

class AwrRepoProcessModel(MappedBaseModel):
    CustomerCode: str
    Dbid: int64
    Cdb: bool
    BeginSnap: int32
    BeginTime: datetime
    EndSnap: int32
    EndTime: datetime

    key_map = {
        "CUS_CODE" : "CustomerCode",
        "DBID" : "CdbDbid",
        "CDB" : "Cdb",
        "BEGIN_SNAP" : "BeginSnap",
        "BEGIN_TIME" : "BeginTime",
        "END_SNAP" : "EndSnap",
        "END_TIME" : "EndTime",
    }