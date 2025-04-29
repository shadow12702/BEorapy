from base.domain.base_entity import BaseEntity
from datetime import datetime

class CdbSqlSnapPhysicalReadMb(BaseEntity):

    DbName: str
    InstanceName: str
    PdbName: str
    SnapTime: datetime
    SqlId: str
    PhysicalReadMb: object
    PhysicalReadMbExec: object

    key_map = {
        'DB_NAME': 'DbName',
        'INSTANCE_NAME': 'InstanceName',
        'PDB_NAME': 'PdbName',
        'SNAP_TIME': 'SnapTime',
        'SQL_ID': 'SqlId',
        'PHYREAD_MB': 'PhysicalReadMb',
        'PHYREAD_MB_EXEC': 'PhysicalReadMbExec'
    }

    def __init__(self, **kwargs):
        """
        CdbSqlSnapPhysicalReadMb model, inheriting from BaseModel.

        Args:
            **kwargs: The kwargs for CdbSqlSnapPhysicalReadMb.
        """
        super().__init__(**kwargs)
