from base.domain.base_entity import BaseEntity
from datetime import datetime
from numpy import float64

class OdbAshTopSqlCostBySnap(BaseEntity):
    
    InstanceName: str
    DbName: str
    SnapId: float64
    Endtime: datetime
    SqlId: str
    Plan: float64
    Cpu: float64
    Wait: float64
    Io: float64
    Total: float64
    PctIo: float64
    PctIoObj: str


    key_map = {        
        'DB_NAME' : 'DbName',
        'INSTANCE_NAME' : 'InstanceName',
        'SNAP_ID' : 'SnapId',
        'ENDTIME' : 'Endtime',
        'SQL_ID' : 'SqlId',
        'PLAN' : 'Plan',
        'CPU' : 'Cpu',
        'WAIT' : 'Wait',
        'IO' : 'Io',
        'TOTAL' : 'Total',
        'PCT_IO' : 'PctIo',
        'PCT_IO_OBJ' : 'PctIoObj'
    }

    def __init__(self, **kwargs):
        """
        OdbAshTopSqlCostBySnap model, inheriting from BaseModel.

        Args:
            **kwargs: The kwargs for OdbAshTopSqlCostBySnap.
        """
        super().__init__(**kwargs)
