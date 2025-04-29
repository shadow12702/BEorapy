from base.domain.base_entity import BaseEntity
from datetime import datetime
from numpy import float64

class NonCdbSegmentSnapPhysicalRead(BaseEntity):

    DbName: str
    InstanceName: str
    SnapTime: datetime
    Owner: str
    ObjectName: str
    PhysicalRead: float64
    Ratio: float64

    key_map = {
        'DB_NAME': 'DbName',
        'INSTANCE_NAME': 'InstanceName',
        'SNAP_TIME': 'SnapTime',
        'OWNER': 'Owner',
        'OBJECT_NAME': 'ObjectName',
        'PHYREAD': 'PhysicalRead',
        'RATIO': 'Ratio'
    }

    def __init__(self, **kwargs):
        """
        NonCdbSegmentSnapPhysicalRead model, inheriting from BaseModel.

        Args:
            **kwargs: The kwargs for NonCdbSegmentSnapPhysicalRead.
        """
        super().__init__(**kwargs)
