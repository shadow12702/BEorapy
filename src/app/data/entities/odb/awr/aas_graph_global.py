from base.domain.base_entity import BaseEntity
from datetime import datetime
from numpy import float64

class OdbAwrAasGraphGlobal(BaseEntity):

    Dbid: float64
    SnapId: float64
    SnapTime: datetime
    DbName: str
    DbTime: datetime
    Eslaped: float64
    CpuCore: float64
    Aas: float64

    key_map = {
        'DBID': 'Dbid',
        'SNAP_ID': 'SnapId',
        'SNAP_TIME': 'SnapTime',
        'DB_NAME': 'DbName',
        'DBTIME': 'DbTime',
        'ESLAPED': 'Eslaped',
        'CPUCORE': 'CpuCore',
        'AAS': 'Aas'
    }

    def __init__(self, **kwargs):
        """
        OdbAwrAasGraphGlobal model, inheriting from BaseModel.

        Args:
            **kwargs: The kwargs for OdbAwrAasGraphGlobal.
        """
        super().__init__(**kwargs)
