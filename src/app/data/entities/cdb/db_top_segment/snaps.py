from base.domain.base_entity import BaseEntity
from datetime import datetime
from numpy import float64

class CdbSegmentSnaps(BaseEntity):

    InstanceName: str
    DbName: str
    PdbName: str
    SnapTime: datetime
    Owner: str
    ObjectName: str
    Value: float64

    key_map = {
        'INSTANCE_NAME': 'InstanceName',
        'DB_NAME': 'DbName',
        'PDB_NAME': 'PdbName',
        'SNAP_TIME': 'SnapTime',
        'OWNER': 'Owner',
        'OBJECT_NAME': 'ObjectName',
        'VALUE': 'Value'
    }

    def __init__(self, **kwargs):
        """
        CdbSegmentSnaps model, inheriting from BaseModel.

        Args:
            **kwargs: The kwargs for CdbSegmentSnaps.
        """
        super().__init__(**kwargs)
