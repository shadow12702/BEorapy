from base.domain.base_entity import BaseEntity
from datetime import datetime
from numpy import float64

class NonCdbSqlSnapAppWait(BaseEntity):

    DbName: str
    InstanceName: str
    SnapTime: datetime
    SqlId: str
    Executions: object
    AppWait: object
    AppWaitExec: object
    Ratio: float64

    key_map = {
        'DB_NAME': 'DbName',
        'INSTANCE_NAME': 'InstanceName',
        'SNAP_TIME': 'SnapTime',
        'SQL_ID': 'SqlId',
        'EXECUTIONS': 'Executions',
        'APPWAIT': 'AppWait',
        'APPWAIT_EXEC': 'AppWaitExec',
        'RATIO': 'Ratio'
    }

    def __init__(self, **kwargs):
        """
        NonCdbSqlSnapAppWait model, inheriting from BaseModel.

        Args:
            **kwargs: The kwargs for NonCdbSqlSnapAppWait.
        """
        super().__init__(**kwargs)
