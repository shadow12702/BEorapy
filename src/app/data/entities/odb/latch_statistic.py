from base.domain.base_entity import BaseEntity
from datetime import datetime

class OdbLatchStatistic(BaseEntity):

    DbName: str
    InstanceName: str
    SnapTime: datetime
    LatchName: str
    Gets: object
    Misses: object
    Sleeps: object

    key_map = {
        'DB_NAME': 'DbName',
        'INSTANCE_NAME': 'InstanceName',
        'SNAP_TIME': 'SnapTime',
        'LATCH_NAME': 'LatchName',
        'GETS': 'Gets',
        'MISSES': 'Misses',
        'SLEEPS': 'Sleeps'
    }

    def __init__(self, **kwargs):
        """
        OdbLatchStatistic model, inheriting from BaseModel.

        Args:
            **kwargs: The kwargs for OdbLatchStatistic.
        """
        super().__init__(**kwargs)
