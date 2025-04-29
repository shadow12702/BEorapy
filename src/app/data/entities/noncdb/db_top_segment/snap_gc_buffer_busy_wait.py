from base.domain.base_entity import BaseEntity
from datetime import datetime
from numpy import float64

class NonCdbSegmentSnapGcBufferBusyWait(BaseEntity):

    DbName: str
    InstanceName: str
    SnapTime: datetime
    Owner: str
    ObjectName: str
    GcBufferBusy: object
    Ratio: float64

    key_map = {
        'DB_NAME': 'DbName',
        'INSTANCE_NAME': 'InstanceName',
        'SNAP_TIME': 'SnapTime',
        'OWNER': 'Owner',
        'OBJECT_NAME': 'ObjectName',
        'GCBUFFERBUSY': 'GcBufferBusy',
        'RATIO': 'Ratio'
    }

    def __init__(self, **kwargs):
        """
        NonCdbSegmentSnapGcBufferBusyWait model, inheriting from BaseModel.

        Args:
            **kwargs: The kwargs for NonCdbSegmentSnapGcBufferBusyWait.
        """
        super().__init__(**kwargs)
