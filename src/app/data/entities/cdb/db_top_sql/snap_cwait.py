from base.domain.base_entity import BaseEntity
from datetime import datetime

class CdbSqlSnapCwait(BaseEntity):

    DbName: str
    InstanceName: str
    PdbName: str
    SnapTime: datetime
    SqlId: str
    ClusterWait: object
    ClusterWaitExec: object

    key_map = {
        'DB_NAME': 'DbName',
        'INSTANCE_NAME': 'InstanceName',
        'PDB_NAME': 'PdbName',
        'SNAP_TIME': 'SnapTime',
        'SQL_ID': 'SqlId',
        'CLUSTERWAIT': 'ClusterWait',
        'CLUSTERWAIT_EXEC': 'ClusterWaitExec'
    }

    def __init__(self, **kwargs):
        """
        CdbSqlSnapCwait model, inheriting from BaseModel.

        Args:
            **kwargs: The kwargs for CdbSqlSnapCwait.
        """
        super().__init__(**kwargs)
