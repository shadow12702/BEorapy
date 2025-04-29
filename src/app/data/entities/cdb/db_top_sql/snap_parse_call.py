from base.domain.base_entity import BaseEntity
from datetime import datetime

class CdbSqlSnapParseCall(BaseEntity):

    DbName: str
    InstanceName: str
    PdbName: str
    SnapTime: datetime
    SqlId: str
    ParseCall: object
    ParseCallExec: object

    key_map = {
        'DB_NAME': 'DbName',
        'INSTANCE_NAME': 'InstanceName',
        'PDB_NAME': 'PdbName',
        'SNAP_TIME': 'SnapTime',
        'SQL_ID': 'SqlId',
        'PARSECALL': 'ParseCall',
        'PARSECALL_EXEC': 'ParseCallExec'
    }

    def __init__(self, **kwargs):
        """
        CdbSqlSnapParseCall model, inheriting from BaseModel.

        Args:
            **kwargs: The kwargs for CdbSqlSnapParseCall.
        """
        super().__init__(**kwargs)
