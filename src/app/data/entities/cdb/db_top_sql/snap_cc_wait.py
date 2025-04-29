from base.domain.base_entity import BaseEntity
from datetime import datetime
from numpy import float64

class CdbSqlSnapCcWait(BaseEntity):

    DbName: str
    InstanceName: str
    PdbName: str
    SnapTime: datetime
    SqlId: str
    CcWait: float64
    CcWaitExec: float64

    key_map = {
        'DB_NAME': 'DbName',
        'INSTANCE_NAME': 'InstanceName',
        'PDB_NAME': 'PdbName',
        'SNAP_TIME': 'SnapTime',
        'SQL_ID': 'SqlId',
        'CCWAIT': 'CcWait',
        'CCWAIT_EXEC': 'CcWaitExec'
    }

    def __init__(self, **kwargs):
        """
        CdbSqlSnapCcWait model, inheriting from BaseModel.

        Args:
            **kwargs: The kwargs for CdbSqlSnapCcWait.
        """
        super().__init__(**kwargs)
