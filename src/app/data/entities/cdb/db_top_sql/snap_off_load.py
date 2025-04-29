from base.domain.base_entity import BaseEntity
from datetime import datetime

class CdbSqlSnapOffLoad(BaseEntity):

    DbName: str
    InstanceName: str
    PdbName: str
    SnapTime: datetime
    SqlId: str
    OffLoad: object
    OffLoadExec: object

    key_map = {
        'DB_NAME': 'DbName',
        'INSTANCE_NAME': 'InstanceName',
        'PDB_NAME': 'PdbName',
        'SNAP_TIME': 'SnapTime',
        'SQL_ID': 'SqlId',
        'OFFLOAD': 'OffLoad',
        'OFFLOAD_EXEC': 'OffLoadExec'
    }

    def __init__(self, **kwargs):
        """
        CdbSqlSnapOffLoad model, inheriting from BaseModel.

        Args:
            **kwargs: The kwargs for CdbSqlSnapOffLoad.
        """
        super().__init__(**kwargs)
