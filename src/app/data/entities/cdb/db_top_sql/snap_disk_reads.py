from base.domain.base_entity import BaseEntity
from datetime import datetime
from numpy import float64

class CdbSqlSnapDiskReads(BaseEntity):

    DbName: str
    InstanceName: str
    PdbName: str
    SnapTime: datetime
    SqlId: str
    DirectReads: object
    DirectReadsExec: object

    key_map = {
        'DB_NAME': 'DbName',
        'INSTANCE_NAME': 'InstanceName',
        'PDB_NAME': 'PdbName',
        'SNAP_TIME': 'SnapTime',
        'SQL_ID': 'SqlId',
        'DIRECT_READS': 'DirectReads',
        'DIRECT_READS_EXEC': 'DirectReadsExec'
    }

    def __init__(self, **kwargs):
        """
        CdbSqlSnapDiskReads model, inheriting from BaseModel.

        Args:
            **kwargs: The kwargs for CdbSqlSnapDiskReads.
        """
        super().__init__(**kwargs)
