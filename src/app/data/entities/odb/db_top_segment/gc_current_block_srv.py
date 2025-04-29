from base.domain.base_entity import BaseEntity
from numpy import float64

class OdbSegmentGcCurrentBlockSrv(BaseEntity):

    DbName: str
    InstanceName: str
    Owner: str
    ObjectName: str
    GcCurrentBlockSrv: float64

    key_map = {
        'DB_NAME': 'DbName',
        'INSTANCE_NAME': 'InstanceName',
        'OWNER': 'Owner',
        'OBJECT_NAME': 'ObjectName',
        'GCCURRENTBLOCKSRV': 'GcCurrentBlockSrv'
    }

    def __init__(self, **kwargs):
        """
        OdbSegmentGcCurrentBlockSrv model, inheriting from BaseModel.

        Args:
            **kwargs: The kwargs for OdbSegmentGcCurrentBlockSrv.
        """
        super().__init__(**kwargs)
