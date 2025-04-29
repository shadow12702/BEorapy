from base.domain.base_entity import BaseEntity
from datetime import datetime
from numpy import float64

class CdbSqlPhysicalWriteDirIops(BaseEntity):

    DbName: str
    InstanceName: str
    PdbName: str
    SqlId: str
    PhysicalWriteDir: object
    PhysicalWriteDirExec: object
    SqlText: str

    key_map = {
        'DB_NAME': 'DbName',
        'INSTANCE_NAME': 'InstanceName',
        'PDB_NAME': 'PdbName',
        'SQL_ID': 'SqlId',
        'PHYWR_DIR': 'PhysicalWriteDir',
        'PHYWR_DIR_EXEC': 'PhysicalWriteDirExec',
        'SQL_TEXT': 'SqlText'
    }

    def __init__(self, **kwargs):
        """
        CdbSqlPhysicalWritedirIops model, inheriting from BaseModel.

        Args:
            **kwargs: The kwargs for CdbSqlPhysicalWritedirIops.
        """
        super().__init__(**kwargs)
