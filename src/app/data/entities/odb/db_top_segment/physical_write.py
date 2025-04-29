from base.domain.base_entity import BaseEntity
from numpy import float64

class OdbSegmentPhysicalWrite(BaseEntity):

    DbName: str
    InstanceName: str
    Owner: str
    ObjectName: str
    PhysicalWrite: float64

    key_map = {
        'DB_NAME': 'DbName',
        'INSTANCE_NAME': 'InstanceName',
        'OWNER': 'Owner',
        'OBJECT_NAME': 'ObjectName',
        'PHYSICALWRITE': 'PhysicalWrite'
    }

    def __init__(self, **kwargs):
        """
        OdbSegmentPhysicalWrite model, inheriting from BaseModel.

        Args:
            **kwargs: The kwargs for OdbSegmentPhysicalWrite.
        """
        super().__init__(**kwargs)
