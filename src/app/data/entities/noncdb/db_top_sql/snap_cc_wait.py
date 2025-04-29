from base.domain.base_entity import BaseEntity
from datetime import datetime
from numpy import float64

class NonCdbSqlSnapCcWait(BaseEntity):

    DbName: str
    InstanceName: str
    SnapTime: datetime
    SqlId: str
    Executions: object
    CcWait: object
    CcWaitExec: object
    Ratio: float64

    key_map = {
        'DB_NAME': 'DbName',
        'INSTANCE_NAME': 'InstanceName',
        'SNAP_TIME': 'SnapTime',
        'SQL_ID': 'SqlId',
        'EXECUTIONS': 'Executions',
        'CCWAIT': 'CcWait',
        'CCWAIT_EXEC': 'CcWaitExec',
        'RATIO': 'Ratio'
    }

    def __init__(self, **kwargs):
        """
        NonCdbSqlSnapCcWait model, inheriting from BaseModel.

        Args:
            **kwargs: The kwargs for NonCdbSqlSnapCcWait.
        """
        super().__init__(**kwargs)
