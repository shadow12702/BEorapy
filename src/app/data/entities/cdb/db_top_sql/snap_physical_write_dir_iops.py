from base.domain.base_entity import BaseEntity
from datetime import datetime

class CdbSqlSnapPhysicalWriteDirIops(BaseEntity):

    DbName: str
    InstanceName: str
    PdbName: str
    SnapTime: datetime
    SqlId: str
    PhysicalWriteDir: object
    PhysicalWriteDirExec: object

    key_map = {
        'DB_NAME': 'DbName',
        'INSTANCE_NAME': 'InstanceName',
        'PDB_NAME': 'PdbName',
        'SNAP_TIME': 'SnapTime',
        'SQL_ID': 'SqlId',
        'PHYWR_DIR': 'PhysicalWriteDir',
        'PHYWR_DIR_EXEC': 'PhysicalWriteDirExec'
    }

    def __init__(self, **kwargs):
        """
        CdbSqlSnapPhysicalWriteDirIops model, inheriting from BaseModel.

        Args:
            **kwargs: The kwargs for CdbSqlSnapPhysicalWriteDirIops.
        """
        super().__init__(**kwargs)
