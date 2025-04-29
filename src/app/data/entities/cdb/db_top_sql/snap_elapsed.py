from base.domain.base_entity import BaseEntity
from datetime import datetime

class CdbSqlSnapElapsed(BaseEntity):

    DbName: str
    InstanceName: str
    PdbName: str
    SnapTime: datetime
    SqlId: str
    ElapsedTime: object
    ElapsedTimeExec: object

    key_map = {
        'DB_NAME': 'DbName',
        'INSTANCE_NAME': 'InstanceName',
        'PDB_NAME': 'PdbName',
        'SNAP_TIME': 'SnapTime',
        'SQL_ID': 'SqlId',
        'ELAPSEDTIME': 'ElapsedTime',
        'ELAPSEDTIME_EXEC': 'ElapsedTimeExec'
    }

    def __init__(self, **kwargs):
        """
        CdbSqlSnapElapsed model, inheriting from BaseModel.

        Args:
            **kwargs: The kwargs for CdbSqlSnapElapsed.
        """
        super().__init__(**kwargs)
