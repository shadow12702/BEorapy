from base.domain.base_entity import BaseEntity
from datetime import datetime

class CdbSqlSnapAppWait(BaseEntity):

    DbName: str
    InstanceName: str
    PdbName: str
    SnapTime: datetime
    SqlId: str
    ApWait: object
    ApWaitExec: object

    key_map = {
        'DB_NAME': 'DbName',
        'INSTANCE_NAME': 'InstanceName',
        'PDB_NAME': 'PdbName',
        'SNAP_TIME': 'SnapTime',
        'SQL_ID': 'SqlId',
        'APWAIT': 'ApWait',
        'APWAIT_EXEC': 'ApWaitExec'
    }

    def __init__(self, **kwargs):
        """
        CdbSqlSnapAppWait model, inheriting from BaseModel.

        Args:
            **kwargs: The kwargs for CdbSqlSnapAppWait.
        """
        super().__init__(**kwargs)
