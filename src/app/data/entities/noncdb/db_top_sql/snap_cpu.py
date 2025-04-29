from base.domain.base_entity import BaseEntity
from datetime import datetime
from numpy import float64

class NonCdbSqlSnapCpu(BaseEntity):

    DbName: str
    InstanceName: str
    SnapTime: datetime
    SqlId: str
    Executions: object
    CpuTime: object
    CpuTimeExec: object
    Ratio: float64

    key_map = {
        'DB_NAME': 'DbName',
        'INSTANCE_NAME': 'InstanceName',
        'SNAP_TIME': 'SnapTime',
        'SQL_ID': 'SqlId',
        'CPUTIME': 'Cputime',
        'EXECUTIONS': 'Executions',
        'CPUTIME_EXEC': 'CputimeExec',
        'RATIO': 'Ratio'
    }

    def __init__(self, **kwargs):
        """
        NonCdbSqlSnapCpu model, inheriting from BaseModel.

        Args:
            **kwargs: The kwargs for NonCdbSqlSnapCpu.
        """
        super().__init__(**kwargs)
