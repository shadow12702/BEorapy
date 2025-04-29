from base.domain.base_entity import BaseEntity
from datetime import datetime

class CdbSqlSnapPhysicalWriteMb(BaseEntity):

    DbName: str
    InstanceName: str
    PdbName: str
    SnapTime: datetime
    SqlId: str
    PhysicalWriteMb: object
    PhysicalWriteMbExec: object

    key_map = {
        'DB_NAME': 'DbName',
        'INSTANCE_NAME': 'InstanceName',
        'PDB_NAME': 'PdbName',
        'SNAP_TIME': 'SnapTime',
        'SQL_ID': 'SqlId',
        'PHYWRITE_MB': 'PhysicalWriteMb',
        'PHYWRITE_MB_EXEC': 'PhysicalWriteExec'
    }

    def __init__(self, **kwargs):
        """
        CdbSqlSnapPhysicalWriteMb model, inheriting from BaseModel.

        Args:
            **kwargs: The kwargs for CdbSqlSnapPhysicalWriteMb.
        """
        super().__init__(**kwargs)
