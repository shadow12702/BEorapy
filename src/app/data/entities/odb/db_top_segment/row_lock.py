from base.domain.base_entity import BaseEntity
from numpy import float64

class OdbSegmentRowLock(BaseEntity):

    DbName: str
    InstanceName: str
    Owner: str
    ObjectName: str
    RowLocks: float64

    key_map = {
        'DB_NAME': 'DbName',
        'INSTANCE_NAME': 'InstanceName',
        'OWNER': 'Owner',
        'OBJECT_NAME': 'ObjectName',
        'ROWLOCKS': 'RowLocks'
    }

    def __init__(self, **kwargs):
        """
        OdbSegmentRowLock model, inheriting from BaseModel.

        Args:
            **kwargs: The kwargs for OdbSegmentRowLock.
        """
        super().__init__(**kwargs)
