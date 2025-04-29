from base.domain.base_entity import BaseEntity
from numpy import float64

class OdbSegmentPhysicalWriteIops(BaseEntity):

    DbName: str
    InstanceName: str
    Owner: str
    ObjectName: str
    PhysicalWriteIops: float64

    key_map = {
        'DB_NAME': 'DbName',
        'INSTANCE_NAME': 'InstanceName',
        'OWNER': 'Owner',
        'OBJECT_NAME': 'ObjectName',
        'PHYSICALWRITE_IOPS': 'PhysicalWriteIops'
    }

    def __init__(self, **kwargs):
        """
        OdbSegmentPhysicalWriteIops model, inheriting from BaseModel.

        Args:
            **kwargs: The kwargs for OdbSegmentPhysicalWriteIops.
        """
        super().__init__(**kwargs)
