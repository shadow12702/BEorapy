from base.domain.base_entity import BaseEntity
from datetime import datetime


class CdbSqlSnapOffLoadReturn(BaseEntity):

    DbName: str
    InstanceName: str
    PdbName: str
    SnapTime: datetime
    SqlId: str
    OffLoadReturn: object
    OffLoadReturnExec: object

    key_map = {
        'DB_NAME': 'DbName',
        'INSTANCE_NAME': 'InstanceName',
        'PDB_NAME': 'PdbName',
        'SNAP_TIME': 'SnapTime',
        'SQL_ID': 'SqlId',
        'OFFLOADRETURN': 'OffLoadReturn',
        'OFFLOADRETURN_EXEC': 'OffLoadReturnExec'
    }

    def __init__(self, **kwargs):
        """
        CdbSqlSnapOffLoadReturn model, inheriting from BaseModel.

        Args:
            **kwargs: The kwargs for CdbSqlSnapOffLoadReturn.
        """
        super().__init__(**kwargs)
