from base.domain.base_entity import BaseEntity
from datetime import datetime
from numpy import float64

class OdbExaAsmDiskgroup(BaseEntity):

    DbName: str
    SnapTime: datetime
    Name: str
    TotalRaw: float64
    FreeRaw: float64
    UsedRaw: float64
    Total: float64
    Free: float64
    Used: float64
    PctFree: float64

    key_map = {
        'DB_NAME': 'DbName',
        'SNAP_TIME': 'SnapTime',
        'NAME': 'Name',
        'TOTALRAW': 'TotalRaw',
        'FREERAW': 'FreeRaw',
        'USEDRAW': 'UsedRaw',
        'TOTAL': 'Total',
        'FREE': 'Free',
        'USED': 'Used',
        'PCT_FREE': 'PctFree'
    }

    def __init__(self, **kwargs):
        """
        OdbExaAsmDiskgroup model, inheriting from BaseModel.

        Args:
            **kwargs: The kwargs for OdbExaAsmDiskgroup.
        """
        super().__init__(**kwargs)
