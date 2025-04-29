from base.domain.base_entity import BaseEntity
from datetime import datetime
from numpy import float64

class OdbExaCellSummary(BaseEntity):

    SnapId: float64
    SnapTime: datetime
    CellName: str
    CpuUsageAvg: float64
    SysUsageAvg: float64
    UserUsageAvg: float64
    RecdMb: float64
    SentMb: float64

    key_map = {
        'SNAP_ID': 'SnapId',
        'SNAP_TIME': 'SnapTime',
        'CELL_NAME': 'CellName',
        'CPU_USAGE_AVG': 'CpuUsageAvg',
        'SYS_USAGE_AVG': 'SysUsageAvg',
        'USER_USAGE_AVG': 'UserUsageAvg',
        'RECD_MB': 'RecdMb',
        'SENT_MB': 'SentMb'
    }

    def __init__(self, **kwargs):
        """
        OdbExaCellSummary model, inheriting from BaseModel.

        Args:
            **kwargs: The kwargs for OdbExaCellSummary.
        """
        super().__init__(**kwargs)
