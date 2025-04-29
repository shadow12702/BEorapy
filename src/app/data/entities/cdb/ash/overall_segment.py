from base.domain.base_entity import BaseEntity
from datetime import datetime
from numpy import float64

class CdbAshOverallSegment(BaseEntity):

    InstanceName: str
    DbName: str
    PdbName: str
    Owner: str
    ObjectName: str
    Pct: float64

    key_map = {
        'OWNER': 'Owner',
        'INSTANCE_NAME': 'InstanceName',
        'DB_NAME': 'DbName',
        'PDB_NAME': 'PdbName',
        'OBJECT_NAME': 'ObjectName',
        'PCT': 'Pct'
    }

    def __init__(self, **kwargs):
        """
        CdbAshOverallSegment model, inheriting from BaseModel.

        Args:
            **kwargs: The kwargs for CdbAshOverallSegment.
        """
        super().__init__(**kwargs)
