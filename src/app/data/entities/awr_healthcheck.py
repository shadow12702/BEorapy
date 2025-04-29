# Description: 

from base.domain.base_entity import BaseEntity
from numpy import int32, int64
from datetime import datetime

class AwrHealthcheck(BaseEntity):
   
    Inst       : int
    Version    : int
    DbName     : str
    CdbDbid    : int64
    PdbDbid    : int64
    PdbName    : str
    BeginSnap  : int32
    BeginTime  : datetime
    EndSnap    : int32
    EndTime    : datetime
    
    key_map = {
        "INST"         : "Inst" ,
        "VERSION"      : "Version" ,
        "DB_NAME"      : "DbName" ,
        "CDB_DBID"     : "CdbDbid" ,
        "PDB_DBID"     : "PdbDbid" ,
        "PDB_NAME"     : "PdbName" ,
        "BEGIN_SNAP"   : "BeginSnap" ,
        "BEGIN_TIME"   : "BeginTime" ,
        "END_SNAP"     : "EndSnap" ,
        "END_TIME"     : "EndTime" 
    }        
