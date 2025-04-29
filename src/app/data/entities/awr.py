from base.domain.base_entity import BaseEntity
from numpy import int32, int64
from datetime import datetime

class Awr(BaseEntity):
   
    Version   : int
    DbName    : str
    Cdb       : str
    CdbDbid   : int64
    PdbDbid   : int64
    PdbName   : str
    BeginSnap : int32
    BeginTime : datetime
    EndSnap   : int32
    EndTime   : datetime
    
    key_map = {
        "VERSION"      : "Version" ,
        "DB_NAME"      : "DbName" ,
        "CDB"          : "Cdb" ,
        "CDB_DBID"     : "CdbDbid" ,
        "PDB_DBID"     : "PdbDbid" ,
        "PDB_NAME"     : "PdbName" ,
        "MIN_SNAP"     : "BeginSnap" ,
        "MINTIME"      : "BeginTime" ,
        "MAX_SNAP"     : "EndSnap" ,
        "MAXTIME"      : "EndTime" 
    }
      
