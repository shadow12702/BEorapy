from base.domain.base_entity import BaseEntity
from datetime import datetime
from numpy import float64

class OdbAshSqlPlanEventBySnap(BaseEntity):

    DbName: str
    InstanceName: str
    SnapId: float64
    Endtime: datetime
    SqlId: str
    Plan: object
    ObjectName: str
    Event: str
    TimeMs: object
    Pct: float64

    key_map = {
        'DB_NAME': 'DbName',
        'INSTANCE_NAME': 'InstanceName',
        'SNAP_ID': 'SnapId',
        'ENDTIME': 'Endtime',
        'SQL_ID': 'SqlId',
        'PLAN': 'Plan',
        'OBJECT_NAME': 'ObjectName',
        'EVENT': 'Event',
        'TIME_MS': 'TimeMs',
        'PCT': 'Pct'
    }

    def __init__(self, **kwargs):
        """
        OdbAshSqlPlanEventBySnap model, inheriting from BaseModel.

        Args:
            **kwargs: The kwargs for OdbAshSqlPlanEventBySnap.
        """
        super().__init__(**kwargs)
