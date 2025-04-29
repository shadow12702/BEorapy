from base.domain.base_entity import BaseEntity
from datetime import datetime
from numpy import float64

class OdbAshTopSegmentBySnap(BaseEntity):

    InstanceName: str
    DbName: str
    SnapId: float64
    Endtime: datetime
    ObjectName: str
    TimeMs: object
    Pct: float64

    key_map = {
        'INSTANCE_NAME': 'InstanceName',
        'DB_NAME': 'DbName',
        'SNAP_ID': 'SnapId',
        'ENDTIME': 'Endtime',
        'OBJECT_NAME': 'ObjectName',
        'TIME_MS': 'TimeMs',
        'PCT': 'Pct'
    }

    def __init__(self, **kwargs):
        """
        OdbAshTopSegmentBySnap model, inheriting from BaseModel.

        Args:
            **kwargs: The kwargs for OdbAshTopSegmentBySnap.
        """
        super().__init__(**kwargs)
