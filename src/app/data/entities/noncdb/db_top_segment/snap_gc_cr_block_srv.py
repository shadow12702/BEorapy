from base.domain.base_entity import BaseEntity
from datetime import datetime
from numpy import float64

class NonCdbSegmentSnapGcCrBlockSrv(BaseEntity):

    DbName: str
    InstanceName: str
    SnapTime: datetime
    Owner: str
    ObjectName: str
    GcCrBlockSrv: float64
    Ratio: float64

    key_map = {
        'DB_NAME': 'DbName',
        'INSTANCE_NAME': 'InstanceName',
        'SNAP_TIME': 'SnapTime',
        'OWNER': 'Owner',
        'OBJECT_NAME': 'ObjectName',
        'GCCRBLOCKSRV': 'GcCrBlockSrv',
        'RATIO': 'Ratio'
    }

    def __init__(self, **kwargs):
        """
        NonCdbSegmentSnapGcCrBlockSrv model, inheriting from BaseModel.

        Args:
            **kwargs: The kwargs for NonCdbSegmentSnapGcCrBlockSrv.
        """
        super().__init__(**kwargs)
