from base.domain.base_entity import BaseEntity
from numpy import float64

class OdbSegmentGcCrBlockRec(BaseEntity):

    InstanceName: str
    DbName: str
    Owner: str
    ObjectName: str
    GcCrBlockRec: float64

    key_map = {
        'DB_NAME': 'DbName',
        'INSTANCE_NAME': 'InstanceName',
        'OWNER': 'Owner',
        'OBJECT_NAME': 'ObjectName',
        'GCCRBLOCKREC': 'GcCrBlockRec'
    }

    def __init__(self, **kwargs):
        """
        OdbSegmentGcCrBlockRec model, inheriting from BaseModel.

        Args:
            **kwargs: The kwargs for OdbSegmentGcCrBlockRec.
        """
        super().__init__(**kwargs)
