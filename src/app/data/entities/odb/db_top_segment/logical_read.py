from base.domain.base_entity import BaseEntity
from numpy import float64

class OdbSegmentLogicalRead(BaseEntity):

    DbName: str
    InstanceName: str
    Owner: str
    ObjectName: str
    LogicalRead: float64

    key_map = {
        'DB_NAME': 'DbName',
        'INSTANCE_NAME': 'InstanceName',
        'OWNER': 'Owner',
        'OBJECT_NAME': 'ObjectName',
        'LOGICALREAD': 'LogicalRead'
    }

    def __init__(self, **kwargs):
        """
        OdbSegmentLogicalRead model, inheriting from BaseModel.

        Args:
            **kwargs: The kwargs for OdbSegmentLogicalRead.
        """
        super().__init__(**kwargs)
