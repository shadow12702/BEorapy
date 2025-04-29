from base.domain.base_entity import BaseEntity
from numpy import float64

class CdbAshOverallSqlWait(BaseEntity):

    InstanceName: str
    DbName: str
    PdbName: str
    SqlId: str
    Pct: float64

    key_map = {
        'INSTANCE_NAME': 'InstanceName',
        'DB_NAME': 'DbName',
        'PDB_NAME': 'PdbName',
        'SQL_ID': 'SqlId',
        'PCT': 'Pct'
    }

    def __init__(self, **kwargs):
        """
        CdbAshOverallSqlWait model, inheriting from BaseModel.

        Args:
            **kwargs: The kwargs for CdbAshOverallSqlWait.
        """
        super().__init__(**kwargs)
