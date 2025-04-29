from base.domain.base_entity import BaseEntity
from numpy import float64

class OdbSegmentGcCurrentBlockRec(BaseEntity):

    DbName: str
    InstanceName: str
    Owner: str
    ObjectName: str
    GcCurrentBlockRec: float64

    key_map = {
        'DB_NAME': 'DbName',
        'INSTANCE_NAME': 'InstanceName',
        'OWNER': 'Owner',
        'OBJECT_NAME': 'ObjectName',
        'GCCURRENTBLOCKREC': 'GcCurrentBlockRec'
    }

    def __init__(self, **kwargs):
        """
        OdbSegmentGcCurrentBlockRec model, inheriting from BaseModel.

        Args:
            **kwargs: The kwargs for OdbSegmentGcCurrentBlockRec.
        """
        super().__init__(**kwargs)
