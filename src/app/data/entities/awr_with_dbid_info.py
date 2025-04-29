from base.domain.base_entity import BaseEntity
from numpy import int32, int64


class AwrWithDbidInfo(BaseEntity):
   
    Dbid   : int64
    InstanceNo : int
    BeginSnap : int32
    EndSnap   : int32    
    
    key_map = {
        'DBID'            : 'Dbid',
        'INSTANCE_NUMBER' : 'InstanceNo',
        'BEGIN_SNAP_ID'   : 'BeginSnap',
        'END_SNAP_ID'     : 'EndSnap'
    }
      