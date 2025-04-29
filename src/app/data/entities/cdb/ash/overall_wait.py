from base.domain.base_entity import BaseEntity
from numpy import float64

class CdbAshOverallWait(BaseEntity):

    InstanceName: str
    DbName: str
    PdbName: str
    Pct: float64

    key_map = {
        'INSTANCE_NAME': 'InstanceName',
        'DB_NAME': 'DbName',
        'PDB_NAME': 'PdbName',
        'PCT': 'Pct'
    }

    def __init__(self, **kwargs):
        """
        CdbAshOverallWait model, inheriting from BaseModel.

        Args:
            **kwargs: The kwargs for CdbAshOverallWait.
        """
        super().__init__(**kwargs)
