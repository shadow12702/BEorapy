from base.domain.base_entity import BaseEntity
from datetime import datetime
from numpy import float64

class NonCdbSqlSnapDiskReads(BaseEntity):

    DbName: str
    InstanceName: str
    SnapTime: datetime
    SqlId: str
    Executions: object
    DirectRead: object
    DirectReadExec: object
    Ratio: float64

    key_map = {
        'DB_NAME': 'DbName',
        'INSTANCE_NAME': 'InstanceName',
        'SNAP_TIME': 'SnapTime',
        'SQL_ID': 'SqlId',
        'EXECUTIONS': 'Executions',
        'DIRECT_READ': 'DirectRead',
        'DIRECT_READ_EXEC': 'DirectReadExec',
        'RATIO': 'Ratio'
    }

    def __init__(self, **kwargs):
        """
        NonCdbSqlSnapDiskReads model, inheriting from BaseModel.

        Args:
            **kwargs: The kwargs for NonCdbSqlSnapDiskReads.
        """
        super().__init__(**kwargs)
