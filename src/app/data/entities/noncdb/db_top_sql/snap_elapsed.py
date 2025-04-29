from base.domain.base_entity import BaseEntity
from datetime import datetime
from numpy import float64

class NonCdbSqlSnapElapsed(BaseEntity):

    DbName: str
    InstanceName: str
    SnapTime: datetime
    SqlId: str
    Executions: object
    ElapsedTimeExec: object
    ElapsedTime: object
    Ratio: float64

    key_map = {
        'DB_NAME': 'DbName',
        'INSTANCE_NAME': 'InstanceName',
        'SNAP_TIME': 'SnapTime',
        'SQL_ID': 'SqlId',
        'EXECUTIONS': 'Executions',
        'ELAPSEDTIME': 'ElapsedTime',
        'ELAPSEDTIME_EXEC': 'ElapsedTimeExec',
        'RATIO': 'Ratio'
    }

    def __init__(self, **kwargs):
        """
        NonCdbSqlSnapElapsed model, inheriting from BaseModel.

        Args:
            **kwargs: The kwargs for NonCdbSqlSnapElapsed.
        """
        super().__init__(**kwargs)
