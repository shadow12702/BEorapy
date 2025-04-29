# Description: 

from base.domain.base_entity import BaseEntity
from datetime import datetime
from numpy import int64, int32

class AwrConfig(BaseEntity):

    Inst      : int = 1;
    TopSql    : str = 'N'
    BeginSnap : int32
    BeginTime : datetime
    EndSnap	  : int32 
    EndTime   : datetime
    Dbid	  : int64
    Version	  : int
    Rac		  : str 
    Exa		  : str
    DbName	  : str
    BlockSize : int
    Cdb		  : str

    key_map = {        
        "BEGIN_SNAP"   : "BeginSnap",
        "BEGIN_TIME"   : "BeginTime",
        "END_SNAP"     : "EndSnap",
        "END_TIME"     : "EndTime",
        "DBID"         : "Dbid",
        "VERSION"      : "Version",
        "RAC"          : "Rac",
        "EXA"          : "Exa",
        "DB_NAME"      : "DbName",
        "BLOCK_SIZE"   : "BlockSize",
        "CDB"          : "Cdb"
    }
    
    @property
    def getAwrConfig(self):
        '''Get Awr Config
        
        :return: configuration string of Awr
        '''
        result = f"BeginSnap={self.BeginSnap};BeginTime={self.BeginTime};EndSnap={self.EndSnap};EndTime={self.EndTime};Inst={self.Inst};DBID={self.Dbid};VERSION='{self.Version}';RAC='{self.Rac}';EXA={self.Exa};DbName={self.DbName};BlockSize={self.BlockSize};TopSql={self.TopSql};CDB='{self.Cdb}';"
        return result
    
    