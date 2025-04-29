from base.domain.base_entity import BaseEntity
from datetime import datetime
from numpy import float64

class OdbAshSqlEventBySnap(BaseEntity):

    DbName: str
    InstanceName: str
    SnapId: float64
    Endtime: datetime
    SqlId: str
    Event: str
    TimeMs: object
    Pct: float64

    key_map = {
        'INSTANCE_NAME': 'InstanceName',
        'DB_NAME': 'DbName',
        'SNAP_ID': 'SnapId',
        'ENDTIME': 'Endtime',
        'SQL_ID': 'SqlId',
        'EVENT': 'Event',
        'TIME_MS': 'TimeMs',
        'PCT': 'Pct'
    }

    def __init__(self, **kwargs):
        """
        OdbAshSqlEventBySnap model, inheriting from BaseModel.

        Args:
            **kwargs: The kwargs for OdbAshSqlEventBySnap.
        """
        super().__init__(**kwargs)
