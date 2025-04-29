from base.domain.base_entity import BaseEntity
from datetime import datetime

class CdbSqlSnapPhysicalWriteIops(BaseEntity):

    DbName: str
    InstanceName: str
    PdbName: str
    SnapTime: datetime
    SqlId: str
    PhysicalWriteReqs: object
    PhysicalWriteReqsExec: object

    key_map = {
        'DB_NAME': 'DbName',
        'INSTANCE_NAME': 'InstanceName',
        'PDB_NAME': 'PdbName',
        'SNAP_TIME': 'SnapTime',
        'SQL_ID': 'SqlId',
        'PHYWR_REQS': 'PhysicalWriteReqs',
        'PHYWR_REQS_EXEC': 'PhysicalWriteReqsExec'
    }

    def __init__(self, **kwargs):
        """
        CdbSqlSnapPhysicalWriteIops model, inheriting from BaseModel.

        Args:
            **kwargs: The kwargs for CdbSqlSnapPhysicalWriteIops.
        """
        super().__init__(**kwargs)
