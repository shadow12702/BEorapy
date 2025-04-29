from base.domain.base_entity import BaseEntity
from numpy import float64

class NonCdbSqlFullScan(BaseEntity):

    SqlId: str
    Plan: float64
    Elapsed: float64
    Cpu: float64
    IoWait: float64
    ClusterWait: float64
    Logical: float64
    Physical: float64
    Execs: float64

    key_map = {
        'SQL_ID': 'SqlId',
        'PLAN': 'Plan',
        'ELAPSED': 'Elapsed',
        'CPU': 'Cpu',
        'IOWAIT': 'IoWait',
        'CLUSTERWAIT': 'ClusterWait',
        'LOGICAL': 'Logical',
        'PHYSICAL': 'Physical',
        'EXECS': 'Execs'
    }

    def __init__(self, **kwargs):
        """
        NonCdbSqlFullScan model, inheriting from BaseModel.

        Args:
            **kwargs: The kwargs for NonCdbSqlFullScan.
        """
        super().__init__(**kwargs)
