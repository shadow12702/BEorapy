from base.domain.base_entity import BaseEntity
from numpy import float64

class CdbSqlAppWait(BaseEntity):

    DbName: str
    InstanceName: str
    PdbName: str
    SqlId: str
    AppWait: float64
    AppWaitExec: float64
    SqlText: float64

    key_map = {
        'DB_NAME': 'DbName',
        'INSTANCE_NAME': 'InstanceName',
        'PDB_NAME': 'PdbName',
        'SQL_ID': 'SqlId',
        'APWAIT': 'AppWait',
        'APWAIT_EXEC': 'AppWaitExec',
        'SQL_TEXT': 'SqlText'
    }

    def __init__(self, **kwargs):
        """
        CdbSqlAppWait model, inheriting from BaseModel.

        Args:
            **kwargs: The kwargs for CdbSqlAppWait.
        """
        super().__init__(**kwargs)
