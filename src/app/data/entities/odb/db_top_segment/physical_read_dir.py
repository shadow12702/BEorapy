from base.domain.base_entity import BaseEntity
from numpy import float64

class OdbSegmentPhysicalReadDir(BaseEntity):

    DbName: str
    InstanceName: str
    Owner: str
    ObjectName: str
    PhysicalReadsDir: float64

    key_map = {
        'DB_NAME': 'DbName',
        'INSTANCE_NAME': 'InstanceName',
        'OWNER': 'Owner',
        'OBJECT_NAME': 'ObjectName',
        'PHYSICALREADS_DIR': 'PhysicalReadsDir'
    }

    def __init__(self, **kwargs):
        """
        OdbSegmentPhysicalReadDir model, inheriting from BaseModel.

        Args:
            **kwargs: The kwargs for OdbSegmentPhysicalReadDir.
        """
        super().__init__(**kwargs)
