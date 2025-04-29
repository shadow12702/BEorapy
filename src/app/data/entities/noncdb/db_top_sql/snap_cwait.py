from base.domain.base_entity import BaseEntity
from datetime import datetime
from numpy import float64

class NonCdbSqlSnapCwait(BaseEntity):

    DbName: str
    InstanceName: str
    SnapTime: datetime
    SqlId: str
    Executions: object
    ClWait: object
    ClWaitExec: object
    Ratio: float64

    key_map = {
        'DB_NAME': 'DbName',
        'INSTANCE_NAME': 'InstanceName',
        'SNAP_TIME': 'SnapTime',
        'SQL_ID': 'SqlId',
        'EXECUTIONS': 'Executions',
        'CLWAIT': 'ClWait',
        'CLWAIT_EXEC': 'ClWaitExec',
        'RATIO': 'Ratio'
    }

    def __init__(self, **kwargs):
        """
        NonCdbSqlSnapCwait model, inheriting from BaseModel.

        Args:
            **kwargs: The kwargs for NonCdbSqlSnapCwait.
        """
        super().__init__(**kwargs)
