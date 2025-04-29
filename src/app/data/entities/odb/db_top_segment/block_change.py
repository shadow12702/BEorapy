from base.domain.base_entity import BaseEntity
from numpy import float64

class OdbSegmentBlockChange(BaseEntity):

    InstanceName: str
    DbName: str
    Owner: str
    ObjectName: str
    BlockChanges: float64

    key_map = {
        'INSTANCE_NAME': 'InstanceName',
        'DB_NAME': 'DbName',
        'OWNER': 'Owner',
        'OBJECT_NAME': 'ObjectName',
        'BLOCKCHANGES': 'BlockChanges'
    }

    def __init__(self, **kwargs):
        """
        OdbSegmentBlockChange model, inheriting from BaseModel.

        Args:
            **kwargs: The kwargs for OdbSegmentBlockChange.
        """
        super().__init__(**kwargs)
