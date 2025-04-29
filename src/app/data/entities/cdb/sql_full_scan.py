from base.domain.base_entity import BaseEntity
from numpy import float64

class CdbSqlFullScan(BaseEntity):

    PdbName: str
    SqlId: str
    Plan: float64
    Elapsed: float64
    Cpu: float64
    IoWait: float64
    ClusterWait: float64
    Logical: float64
    Physical: float64

    key_map = {
        'PDB_NAME': 'PdbName',
        'SQL_ID': 'SqlId',
        'PLAN': 'Plan',
        'ELAPSED': 'Elapsed',
        'CPU': 'Cpu',
        'IOWAIT': 'IoWait',
        'CLUSTERWAIT': 'ClusterWait',
        'LOGICAL': 'Logical',
        'PHYSICAL': 'Physical'
    }

    def __init__(self, **kwargs):
        """
        CdbSqlFullScan model, inheriting from BaseModel.

        Args:
            **kwargs: The kwargs for CdbSqlFullScan.
        """
        super().__init__(**kwargs)
