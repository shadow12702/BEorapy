from base.domain.base_entity import BaseEntity
from numpy import float64

class OdbSegmentGcCrBlockSrv(BaseEntity):

    DbName: str
    InstanceName: str
    Owner: str
    ObjectName: str
    GcCrBlockSrv: float64

    key_map = {
        'DB_NAME': 'DbName',
        'INSTANCE_NAME': 'InstanceName',
        'OWNER': 'Owner',
        'OBJECT_NAME': 'ObjectName',
        'GCCRBLOCKSRV': 'GcCrBlockSrv'
    }

    def __init__(self, **kwargs):
        """
        OdbSegmentGcCrBlockSrv model, inheriting from BaseModel.

        Args:
            **kwargs: The kwargs for OdbSegmentGcCrBlockSrv.
        """
        super().__init__(**kwargs)
