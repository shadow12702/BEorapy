from base.domain.base_entity import BaseEntity
from datetime import datetime
from numpy import float64

class OdbSgaStatistic(BaseEntity):

    DbName: str
    InstanceName: str
    SnapTime: datetime
    Sga: float64
    Bc: float64
    Spt: float64
    Jp: float64
    Lp: float64
    Stp: float64
    Imp: float64

    key_map = {
        'DB_NAME': 'DbName',
        'INSTANCE_NAME': 'InstanceName',
        'SNAP_TIME': 'SnapTime',
        'SGA': 'Sga',
        'BC': 'Bc',
        'SPT': 'Spt',
        'JP': 'Jp',
        'LP': 'Lp',
        'STP': 'Stp',
        'IMP': 'Imp'
    }

    def __init__(self, **kwargs):
        """
        OdbSgaStatistic model, inheriting from BaseModel.

        Args:
            **kwargs: The kwargs for OdbSgaStatistic.
        """
        super().__init__(**kwargs)
