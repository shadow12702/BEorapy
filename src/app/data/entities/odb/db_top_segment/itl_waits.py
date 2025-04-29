from base.domain.base_entity import BaseEntity
from numpy import float64

class OdbSegmentItlWaits(BaseEntity):

    DbName: str
    InstanceName: str
    Owner: str
    ObjectName: str
    ItlWaits: float64

    key_map = {
        'DB_NAME': 'DbName',
        'INSTANCE_NAME': 'InstanceName',
        'OWNER': 'Owner',
        'OBJECT_NAME': 'ObjectName',
        'ITL_WAITS': 'ItlWaits'
    }

    def __init__(self, **kwargs):
        """
        OdbSegmentItlWaits model, inheriting from BaseModel.

        Args:
            **kwargs: The kwargs for OdbSegmentItlWaits.
        """
        super().__init__(**kwargs)
