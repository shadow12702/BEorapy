from base.domain.base_entity import BaseEntity
from datetime import datetime
from numpy import float64

class OdbAshSqlPlanChange(BaseEntity):

    SqlId: str
    PlanHashValue: object
    AvgTime: datetime
    AvgCpu: float64
    AvgIowait: float64
    AvgCluster: float64
    AvgBuffer: float64
    AvgDisk: float64

    key_map = {
        'SQL_ID': 'SqlId',
        'PLAN_HASH_VALUE': 'PlanHashValue',
        'AVG_TIME': 'AvgTime',
        'AVG_CPU': 'AvgCpu',
        'AVG_IOWAIT': 'AvgIowait',
        'AVG_CLUSTER': 'AvgCluster',
        'AVG_BUFFER': 'AvgBuffer',
        'AVG_DISK': 'AvgDisk'
    }

    def __init__(self, **kwargs):
        """
        OdbAshSqlPlanChange model, inheriting from BaseModel.

        Args:
            **kwargs: The kwargs for OdbAshSqlPlanChange.
        """
        super().__init__(**kwargs)
