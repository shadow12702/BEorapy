from base.domain.base_entity import BaseEntity
from datetime import datetime
from numpy import float64

class OdbAshTopSegmentSqlEventBySnap(BaseEntity):

    InstanceName: str
    DbName: str
    SnapId: float64
    Endtime: datetime
    SqlId: str
    ObjectName: str
    Event: str
    TimeMs: object
    Pct: float64

    key_map = {
        'INSTANCE_NAME': 'InstanceName',
        'DB_NAME': 'DbName',
        'SNAP_ID': 'SnapId',
        'ENDTIME': 'Endtime',
        'SQL_ID': 'SqlId',
        'OBJECT_NAME': 'ObjectName',
        'EVENT': 'Event',
        'TIME_MS': 'TimeMs',
        'PCT': 'Pct'
    }

    def __init__(self, **kwargs):
        """
        OdbAshTopSegmentSqlEventBySnap model, inheriting from BaseModel.

        Args:
            **kwargs: The kwargs for OdbAshTopSegmentSqlEventBySnap.
        """
        super().__init__(**kwargs)
