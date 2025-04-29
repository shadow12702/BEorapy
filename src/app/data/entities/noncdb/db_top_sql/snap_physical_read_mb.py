from base.domain.base_entity import BaseEntity
from datetime import datetime
from numpy import float64

class NonCdbSqlSnapPhysicalReadMb(BaseEntity):

    DbName: str
    InstanceName: str
    SnapTime: datetime
    SqlId: str
    Executions: object
    PhysicalReadMb: object
    PhysicalReadMbExec: object
    Ratio: float64

    key_map = {
        'DB_NAME': 'DbName',
        'INSTANCE_NAME': 'InstanceName',
        'SNAP_TIME': 'SnapTime',
        'SQL_ID': 'SqlId',
        'EXECUTIONS': 'Executions',
        'PHYREAD_MB': 'PhysicalReadMb',
        'PHYREAD_MB_EXEC': 'PhysicalReadMbExec',
        'RATIO': 'Ratio'
    }

    def __init__(self, **kwargs):
        """
        NonCdbSqlSnapPhysicalReadMb model, inheriting from BaseModel.

        Args:
            **kwargs: The kwargs for NonCdbSqlSnapPhysicalReadMb.
        """
        super().__init__(**kwargs)
