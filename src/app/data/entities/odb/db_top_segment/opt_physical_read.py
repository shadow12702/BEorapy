from base.domain.base_entity import BaseEntity
from numpy import float64

class OdbSegmentOptPhysicalRead(BaseEntity):

    DbName: str
    InstanceName: str
    Owner: str
    ObjectName: str
    OptPhysicalReads: float64

    key_map = {
        'DB_NAME': 'DbName',
        'INSTANCE_NAME': 'InstanceName',
        'OWNER': 'Owner',
        'OBJECT_NAME': 'ObjectName',
        'OPTPHYSICALREADS': 'OptPhysicalReads'
    }

    def __init__(self, **kwargs):
        """
        OdbSegmentOptPhysicalRead model, inheriting from BaseModel.

        Args:
            **kwargs: The kwargs for OdbSegmentOptPhysicalRead.
        """
        super().__init__(**kwargs)
