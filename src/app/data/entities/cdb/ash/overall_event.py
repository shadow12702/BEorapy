from base.domain.base_entity import BaseEntity
from datetime import datetime
from numpy import float64

class CdbAshOverallEvent(BaseEntity):

    InstanceName: str
    DbName: str
    PdbName: str
    Event: str
    Pct: float64

    key_map = {
        'INSTANCE_NAME': 'InstanceName',
        'DB_NAME': 'DbName',
        'PDB_NAME': 'PdbName',
        'EVENT': 'Event',
        'PCT': 'Pct'
    }

    def __init__(self, **kwargs):
        """
        CdbAshOverallEvent model, inheriting from BaseModel.

        Args:
            **kwargs: The kwargs for CdbAshOverallEvent.
        """
        super().__init__(**kwargs)
