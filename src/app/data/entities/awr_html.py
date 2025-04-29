# Description: 

from base.domain.base_entity import BaseEntity
from numpy import int64

class AwrHtml(BaseEntity):
   
    Dbid   : int64
    InstanceNo : int
    BeginSnap : int64
    EndSnap   : int64    
    
    key_map = {
        'DBID'            : 'Dbid',
        'INSTANCE_NUMBER' : 'InstanceNo',
        'BEGIN_SNAP_ID'   : 'BeginSnap',
        'END_SNAP_ID'     : 'EndSnap'
    }
