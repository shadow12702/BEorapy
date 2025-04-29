from base.domain.base_entity import BaseEntity
from datetime import datetime

class CdbSqlSnapLogicalRead(BaseEntity):

    DbName: str
    InstanceName: str
    PdbName: str
    SnapTime: datetime
    SqlId: str
    LogicalReads: object
    LogicalReadsExec: object

    key_map = {
        'DB_NAME': 'DbName',
        'INSTANCE_NAME': 'InstanceName',
        'PDB_NAME': 'PdbName',
        'SNAP_TIME': 'SnapTime',
        'SQL_ID': 'SqlId',
        'LOGICAL_READS': 'LogicalReads',
        'LOGICAL_READS_EXEC': 'LogicalReadsExec'
    }

    def __init__(self, **kwargs):
        """
        CdbSqlSnapLogicalRead model, inheriting from BaseModel.

        Args:
            **kwargs: The kwargs for CdbSqlSnapLogicalRead.
        """
        super().__init__(**kwargs)
