from base.domain.base_entity import BaseEntity
from datetime import datetime

class CdbSqlSnapInvalid(BaseEntity):

    DbName: str
    InstanceName: str
    PdbName: str
    SnapTime: datetime
    SqlId: str
    Invalid: object
    InvalidExec: object

    key_map = {
        'DB_NAME': 'DbName',
        'INSTANCE_NAME': 'InstanceName',
        'PDB_NAME': 'PdbName',
        'SNAP_TIME': 'SnapTime',
        'SQL_ID': 'SqlId',
        'INVALID': 'Invalid',
        'INVALID_EXEC': 'InvalidExec'
    }

    def __init__(self, **kwargs):
        """
        CdbSqlSnapInvalid model, inheriting from BaseModel.

        Args:
            **kwargs: The kwargs for CdbSqlSnapInvalid.
        """
        super().__init__(**kwargs)
