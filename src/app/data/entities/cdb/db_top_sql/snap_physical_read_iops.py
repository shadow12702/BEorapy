from base.domain.base_entity import BaseEntity
from datetime import datetime

class CdbSqlSnapPhysicalReadIops(BaseEntity):

    DbName: str
    InstanceName: str
    PdbName: str
    SnapTime: datetime
    SqlId: str
    PhysicalReadReqs: object
    PhysicalReadReqsExec: object

    key_map = {
        'DB_NAME': 'DbName',
        'INSTANCE_NAME': 'InstanceName',
        'PDB_NAME': 'PdbName',
        'SNAP_TIME': 'SnapTime',
        'SQL_ID': 'SqlId',
        'PHYRD_REQS': 'PhysicalReadReqs',
        'PHYRD_REQS_EXEC': 'PhysicalReadReqsExec'
    }

    def __init__(self, **kwargs):
        """
        CdbSqlSnapPhysicalReadIops model, inheriting from BaseModel.

        Args:
            **kwargs: The kwargs for CdbSqlSnapPhysicalReadIops.
        """
        super().__init__(**kwargs)
