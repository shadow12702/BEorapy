from base.domain.base_entity import BaseEntity
from datetime import datetime
from numpy import float64

class NonCdbIoFileTypeStatistic(BaseEntity):

    DbName: str
    InstanceName: str
    SnapId: float64
    SnapTime: datetime
    FiletypeName: str
    Mbps: float64
    Iops: float64

    key_map = {
        'DB_NAME': 'DbName',
        'INSTANCE_NAME': 'InstanceName',
        'SNAP_ID': 'SnapId',
        'SNAP_TIME': 'SnapTime',
        'FILETYPE_NAME': 'FiletypeName',
        'MBPS': 'Mbps',
        'IOPS': 'Iops'
    }

    def __init__(self, **kwargs):
        """
        NonCdbIoFileTypeStatistic model, inheriting from BaseModel.

        Args:
            **kwargs: The kwargs for NonCdbIoFileTypeStatistic.
        """
        super().__init__(**kwargs)
