from base.domain.base_entity import BaseEntity
from datetime import datetime
from numpy import float64

class CdbSqlSnapVersions(BaseEntity):

    DbName: str
    InstanceName: str
    PdbName: str
    SnapTime: datetime
    SqlId: str
    Version: float64
    VersionExec: float64

    key_map = {
        'DB_NAME': 'DbName',
        'INSTANCE_NAME': 'InstanceName',
        'PDB_NAME': 'PdbName',
        'SNAP_TIME': 'SnapTime',
        'SQL_ID': 'SqlId',
        'VERSION': 'Version',
        'VERSION_EXEC': 'VersionExec'
    }

    def __init__(self, **kwargs):
        """
        CdbSqlSnapVersions model, inheriting from BaseModel.

        Args:
            **kwargs: The kwargs for CdbSqlSnapVersions.
        """
        super().__init__(**kwargs)
