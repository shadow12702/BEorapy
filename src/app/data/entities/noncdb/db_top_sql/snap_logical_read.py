from base.domain.base_entity import BaseEntity
from datetime import datetime
from numpy import float64

class NonCdbSqlSnapLogicalRead(BaseEntity):

    DbName: str
    InstanceName: str
    SnapTime: datetime
    SqlId: str
    Executions: object
    LogicalRead: object
    LogicalReadExec: object
    Ratio: float64

    key_map = {
        'DB_NAME': 'DbName',
        'INSTANCE_NAME': 'InstanceName',
        'SNAP_TIME': 'SnapTime',
        'SQL_ID': 'SqlId',
        'EXECUTIONS': 'Executions',
        'LOGICALREAD': 'LogicalRead',
        'LOGICALREAD_EXEC': 'LogicalReadExec',
        'RATIO': 'Ratio'
    }

    def __init__(self, **kwargs):
        """
        NonCdbSqlSnapLogicalRead model, inheriting from BaseModel.

        Args:
            **kwargs: The kwargs for NonCdbSqlSnapLogicalRead.
        """
        super().__init__(**kwargs)
