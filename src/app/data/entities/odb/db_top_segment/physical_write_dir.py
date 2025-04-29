from base.domain.base_entity import BaseEntity
from numpy import float64

class OdbSegmentPhysicalWriteDir(BaseEntity):

    DbName: str
    InstanceName: str
    Owner: str
    ObjectName: str
    PhysicalWriteDir: float64

    key_map = {
        'DB_NAME': 'DbName',
        'INSTANCE_NAME': 'InstanceName',
        'OWNER': 'Owner',
        'OBJECT_NAME': 'ObjectName',
        'PHYSICALWRITE_DIR': 'PhysicalWriteDir'
    }

    def __init__(self, **kwargs):
        """
        OdbSegmentPhysicalWriteDir model, inheriting from BaseModel.

        Args:
            **kwargs: The kwargs for OdbSegmentPhysicalWriteDir.
        """
        super().__init__(**kwargs)
