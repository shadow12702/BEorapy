from base.domain.base_entity import BaseEntity
from numpy import float64

class OdbSegmentGcBufferBusyWait(BaseEntity):

    InstanceName: str
    DbName: str
    Owner: str
    ObjectName: str
    GcBufferBusy: float64

    key_map = {
        'INSTANCE_NAME': 'InstanceName',
        'DB_NAME': 'DbName',
        'OWNER': 'Owner',
        'OBJECT_NAME': 'ObjectName',
        'GCBUFFERBUSY': 'GcBufferBusy'
    }

    def __init__(self, **kwargs):
        """
        OdbSegmentGcBufferBusyWait model, inheriting from BaseModel.

        Args:
            **kwargs: The kwargs for OdbSegmentGcBufferBusyWait.
        """
        super().__init__(**kwargs)
