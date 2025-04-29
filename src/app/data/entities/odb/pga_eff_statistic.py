from base.domain.base_entity import BaseEntity
from datetime import datetime
from numpy import float64

class OdbPgaEffStatistic(BaseEntity):

    DbName: str
    InstanceName: str
    SnapTime: datetime
    Multipass: float64
    Optimal: float64
    Onepass: float64
    TotalExec: float64

    key_map = {
        'DB_NAME': 'DbName',
        'INSTANCE_NAME': 'InstanceName',
        'SNAP_TIME': 'SnapTime',
        'MULTIPASS': 'Multipass',
        'OPTIMAL': 'Optimal',
        'ONEPASS': 'Onepass',
        'TOTALEXEC': 'TotalExec'
    }

    def __init__(self, **kwargs):
        """
        OdbPgaEffStatistic model, inheriting from BaseModel.

        Args:
            **kwargs: The kwargs for OdbPgaEffStatistic.
        """
        super().__init__(**kwargs)
