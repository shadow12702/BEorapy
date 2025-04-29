from base.domain.base_entity import BaseEntity
from numpy import float64

class OdbSegmentPhysicalReadIops(BaseEntity):

    DbName: str
    InstanceName: str
    Owner: str
    ObjectName: str
    PhysicalReadsIops: float64

    key_map = {
        'DB_NAME': 'DbName',
        'INSTANCE_NAME': 'InstanceName',
        'OWNER': 'Owner',
        'OBJECT_NAME': 'ObjectName',
        'PHYSICALREADS_IOPS': 'PhysicalReadsIops'
    }

    def __init__(self, **kwargs):
        """
        OdbSegmentPhysicalReadIops model, inheriting from BaseModel.

        Args:
            **kwargs: The kwargs for OdbSegmentPhysicalReadIops.
        """
        super().__init__(**kwargs)
