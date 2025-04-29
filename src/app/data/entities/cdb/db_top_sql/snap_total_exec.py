from base.domain.base_entity import BaseEntity
from datetime import datetime

class CdbSqlSnapTotalExec(BaseEntity):

    DbName: str
    InstanceName: str
    PdbName: str
    SnapTime: datetime
    SqlId: str
    Execs: object

    key_map = {
        'DB_NAME': 'DbName',
        'INSTANCE_NAME': 'InstanceName',
        'PDB_NAME': 'PdbName',
        'SNAP_TIME': 'SnapTime',
        'SQL_ID': 'SqlId',
        'EXECS': 'Execs'
    }

    def __init__(self, **kwargs):
        """
        CdbSqlSnapTotalExec model, inheriting from BaseModel.

        Args:
            **kwargs: The kwargs for CdbSqlSnapTotalExec.
        """
        super().__init__(**kwargs)
