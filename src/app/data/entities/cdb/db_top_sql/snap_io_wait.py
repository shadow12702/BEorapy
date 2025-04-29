from base.domain.base_entity import BaseEntity
from datetime import datetime

class CdbSqlSnapIoWait(BaseEntity):

    DbName: str
    InstanceName: str
    PdbName: str
    SnapTime: datetime
    SqlId: str
    IoWait: object
    IoWaitExec: object

    key_map = {
        'DB_NAME': 'DbName',
        'INSTANCE_NAME': 'InstanceName',
        'PDB_NAME': 'PdbName',
        'SNAP_TIME': 'SnapTime',
        'SQL_ID': 'SqlId',
        'IOWAIT': 'IoWait',
        'IOWAIT_EXEC': 'IoWaitExec'
    }

    def __init__(self, **kwargs):
        """
        CdbSqlSnapIoWait model, inheriting from BaseModel.

        Args:
            **kwargs: The kwargs for CdbSqlSnapIoWait.
        """
        super().__init__(**kwargs)
