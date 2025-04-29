from base.domain.base_entity import BaseEntity
from datetime import datetime

class CdbSqlSnapCpu(BaseEntity):

    DbName: str
    InstanceName: str
    PdbName: str
    SnapTime: datetime
    SqlId: str
    CpuTime: object
    CpuTimeExec: object

    key_map = {
        'DB_NAME': 'DbName',
        'INSTANCE_NAME': 'InstanceName',
        'PDB_NAME': 'PdbName',
        'SNAP_TIME': 'SnapTime',
        'SQL_ID': 'SqlId',
        'CPUTIME': 'Cputime',
        'CPUTIME_EXEC': 'CputimeExec'
    }

    def __init__(self, **kwargs):
        """
        CdbSqlSnapCpu model, inheriting from BaseModel.

        Args:
            **kwargs: The kwargs for CdbSqlSnapCpu.
        """
        super().__init__(**kwargs)
