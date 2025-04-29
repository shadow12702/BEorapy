from base.domain.base_entity import BaseEntity
from datetime import datetime
from numpy import float64

class OdbDbWcAas(BaseEntity):

    SnapId: float64
    SnapTime: datetime
    DbName: str
    InstanceName: str
    WaitClass: object
    Aas: float64
    DbTime: datetime

    key_map = {
        'SNAP_ID': 'SnapId',
        'SNAP_TIME': 'SnapTime',
        'DB_NAME': 'DbName',
        'INSTANCE_NAME': 'InstanceName',
        'WAIT_CLASS': 'WaitClass',
        'AAS': 'Aas',
        'DB_TIME': 'DbTime'
    }

    def __init__(self, **kwargs):
        """
        DbWcAas model, inheriting from BaseModel.

        Args:
            **kwargs: The kwargs for DbWcAas.
        """
        super().__init__(**kwargs)
