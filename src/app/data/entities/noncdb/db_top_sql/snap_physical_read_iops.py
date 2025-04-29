from base.domain.base_entity import BaseEntity
from datetime import datetime
from numpy import float64

class NonCdbSqlSnapPhysicalReadIops(BaseEntity):

    DbName: str
    InstanceName: str
    SnapTime: datetime
    SqlId: str
    Executions: object
    PhysicalReadReq: object
    PhysicalReadReqExec: object
    Ratio: float64

    key_map = {
        'DB_NAME': 'DbName',
        'INSTANCE_NAME': 'InstanceName',
        'SNAP_TIME': 'SnapTime',
        'SQL_ID': 'SqlId',
        'EXECUTIONS': 'Executions',
        'PHYREAD_REQ': 'PhysicalReadReq',
        'PHYREAD_REQ_EXEC': 'PhysicalReadReqExec',
        'RATIO': 'Ratio'
    }

    def __init__(self, **kwargs):
        """
        NonCdbSqlSnapPhysicalReadIops model, inheriting from BaseModel.

        Args:
            **kwargs: The kwargs for NonCdbSqlSnapPhysicalReadIops.
        """
        super().__init__(**kwargs)
