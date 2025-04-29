from base.domain.base_entity import BaseEntity
from datetime import datetime
from numpy import float64

class CdbAshOverallIndex(BaseEntity):

    InstanceName: str
    DbName: str
    PdbName: str
    Owner: str
    ObjectName: str
    Pct: float64

    key_map = {
        'INSTANCE_NAME': 'InstanceName',
        'DB_NAME': 'DbName',
        'PDB_NAME': 'PdbName',
        'OWNER': 'Owner',
        'OBJECT_NAME': 'ObjectName',
        'PCT': 'Pct'
    }

    def __init__(self, **kwargs):
        """
        CdbAshOverallIndex model, inheriting from BaseModel.

        Args:
            **kwargs: The kwargs for CdbAshOverallIndex.
        """
        super().__init__(**kwargs)
