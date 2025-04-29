from base.domain.base_entity import BaseEntity
from datetime import datetime
from numpy import float64

class NonCdbSegmentSnapPhysicalWriteDir(BaseEntity):

    DbName: str
    InstanceName: str
    SnapTime: datetime
    Owner: str
    ObjectName: str
    PhysicalWriteDir: float64
    Ratio: float64

    key_map = {
        'DB_NAME': 'DbName',
        'INSTANCE_NAME': 'InstanceName',
        'SNAP_TIME': 'SnapTime',
        'OWNER': 'Owner',
        'OBJECT_NAME': 'ObjectName',
        'PHYWRITE_DIR': 'PhysicalWriteDir',
        'RATIO': 'Ratio'
    }

    def __init__(self, **kwargs):
        """
        NonCdbSegmentSnapPhysicalWriteDir model, inheriting from BaseModel.

        Args:
            **kwargs: The kwargs for NonCdbSegmentSnapPhysicalWriteDir.
        """
        super().__init__(**kwargs)
