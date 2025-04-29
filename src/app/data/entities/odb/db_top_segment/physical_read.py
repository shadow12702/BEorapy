from base.domain.base_entity import BaseEntity
from numpy import float64

class OdbSegmentPhysicalRead(BaseEntity):

    DbName: str
    InstanceName: str
    Owner: str
    ObjectName: str
    PhysicalReads: float64

    key_map = {
        'DB_NAME': 'DbName',
        'INSTANCE_NAME': 'InstanceName',
        'OWNER': 'Owner',
        'OBJECT_NAME': 'ObjectName',
        'PHYSICALREADS': 'PhysicalReads'
    }

    def __init__(self, **kwargs):
        """
        OdbSegmentPhysicalRead model, inheriting from BaseModel.

        Args:
            **kwargs: The kwargs for OdbSegmentPhysicalRead.
        """
        super().__init__(**kwargs)
