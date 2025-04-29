from base.domain.base_entity import BaseEntity
from datetime import datetime
from numpy import float64

class NonCdbSqlSnapPhysicalWriteIops(BaseEntity):

    DbName: str
    InstanceName: str
    SnapTime: datetime
    SqlId: str
    Executions: object
    PhysicalWriteReq: object
    PhysicalWriteReqExec: object
    Ratio: float64

    key_map = {
        'DB_NAME': 'DbName',
        'INSTANCE_NAME': 'InstanceName',
        'SNAP_TIME': 'SnapTime',
        'SQL_ID': 'SqlId',
        'EXECUTIONS': 'Executions',
        'PHYWRITE_REQ': 'PhysicalWriteReq',
        'PHYWRITE_REQ_EXEC': 'PhysicalWriteReqExec',
        'RATIO': 'Ratio'
    }

    def __init__(self, **kwargs):
        """
        NonCdbSqlSnapPhysicalWriteIops model, inheriting from BaseModel.

        Args:
            **kwargs: The kwargs for NonCdbSqlSnapPhysicalWriteIops.
        """
        super().__init__(**kwargs)
