from base.domain.base_entity import BaseEntity
from datetime import datetime
from numpy import float64

class NonCdbSegmentSnapOptPhysicalRead(BaseEntity):

    DbName: str
    InstanceName: str
    SnapTime: datetime
    Owner: str
    ObjectName: str
    OptPhysicalRead: float64
    Ratio: float64

    key_map = {
        'DB_NAME': 'DbName',
        'INSTANCE_NAME': 'InstanceName',
        'SNAP_TIME': 'SnapTime',
        'OWNER': 'Owner',
        'OBJECT_NAME': 'ObjectName',
        'OPTPHYSICALREAD': 'OptPhysicalRead',
        'RATIO': 'Ratio'
    }

    def __init__(self, **kwargs):
        """
        NonCdbSegmentSnapOptPhysicalRead model, inheriting from BaseModel.

        Args:
            **kwargs: The kwargs for NonCdbSegmentSnapOptPhysicalRead.
        """
        super().__init__(**kwargs)
