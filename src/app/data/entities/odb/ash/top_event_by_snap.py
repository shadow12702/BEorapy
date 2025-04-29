from base.domain.base_entity import BaseEntity
from datetime import datetime
from numpy import float64

class OdbAshTopEventBySnap(BaseEntity):

    InstanceName: str
    DbName: str
    SnapId: float64
    Endtime: datetime
    Event: str
    TimeMs: object
    Pct: float64

    key_map = {
        'INSTANCE_NAME': 'InstanceName',
        'DB_NAME': 'DbName',
        'SNAP_ID': 'SnapId',
        'ENDTIME': 'Endtime',
        'EVENT': 'Event',
        'TIME_MS': 'TimeMs',
        'PCT': 'Pct'
    }

    def __init__(self, **kwargs):
        """
        OdbAshTopEventBySnap model, inheriting from BaseModel.

        Args:
            **kwargs: The kwargs for OdbAshTopEventBySnap.
        """
        super().__init__(**kwargs)
