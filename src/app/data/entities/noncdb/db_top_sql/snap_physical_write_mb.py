from base.domain.base_entity import BaseEntity
from datetime import datetime
from numpy import float64

class NonCdbSqlSnapPhysicalWriteMb(BaseEntity):

    DbName: str
    InstanceName: str
    SnapTime: datetime
    SqlId: str
    Executions: object
    PhysicalWriteMb: object
    PhysicalWriteMbExec: object
    Ratio: float64

    key_map = {
        'DB_NAME': 'DbName',
        'INSTANCE_NAME': 'InstanceName',
        'SNAP_TIME': 'SnapTime',
        'SQL_ID': 'SqlId',
        'EXECUTIONS': 'Executions',
        'PHYWRITE_MB': 'PhysicalWriteMb',
        'PHYWRITE_MB_EXEC': 'PhysicalWriteMbExec',
        'RATIO': 'Ratio'
    }

    def __init__(self, **kwargs):
        """
        NonCdbSqlSnapPhysicalWriteMb model, inheriting from BaseModel.

        Args:
            **kwargs: The kwargs for NonCdbSqlSnapPhysicalWriteMb.
        """
        super().__init__(**kwargs)
