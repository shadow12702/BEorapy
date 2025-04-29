from base.domain.base_entity import BaseEntity
from datetime import datetime
from numpy import float64

class OdbMemConfig(BaseEntity):

    DbName: str
    InstanceName: str
    SnapId: float64
    SnapTime: datetime
    TotalSga: float64
    Sga: float64
    Pga: float64
    DbMem: float64
    Osmem: float64

    key_map = {
        'DB_NAME': 'DbName',
        'INSTANCE_NAME': 'InstanceName',
        'SNAP_ID': 'SnapId',
        'SNAP_TIME': 'SnapTime',
        'TOTALSGA': 'TotalSga',
        'SGA': 'Sga',
        'PGA': 'Pga',
        'DB_MEM': 'DbMem',
        'OSMEM': 'Osmem'
    }

    def __init__(self, **kwargs):
        """
        OdbMemConfig model, inheriting from BaseModel.

        Args:
            **kwargs: The kwargs for OdbMemConfig.
        """
        super().__init__(**kwargs)
