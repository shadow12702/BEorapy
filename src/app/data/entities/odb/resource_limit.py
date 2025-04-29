from base.domain.base_entity import BaseEntity
from datetime import datetime
from numpy import float64

class OdbResourceLimit(BaseEntity):

    DbName: str
    InstanceName: str
    SnapId: float64
    ResourceName: str
    SnapTime: datetime
    Cur: float64
    Max: float64
    Allocate: float64

    key_map = {
        'DB_NAME': 'DbName',
        'INSTANCE_NAME': 'InstanceName',
        'SNAP_ID': 'SnapId',
        'RESOURCE_NAME': 'ResourceName',
        'SNAP_TIME': 'SnapTime',
        'CUR': 'Cur',
        'MAX': 'Max',
        'ALLOCATE': 'Allocate'
    }

    def __init__(self, **kwargs):
        """
        OdbResourceLimit model, inheriting from BaseModel.

        Args:
            **kwargs: The kwargs for OdbResourceLimit.
        """
        super().__init__(**kwargs)
