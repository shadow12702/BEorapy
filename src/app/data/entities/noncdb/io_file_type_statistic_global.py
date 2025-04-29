from base.domain.base_entity import BaseEntity
from datetime import datetime
from numpy import float64

class NonCdbIoFileTypeStatisticGlobal(BaseEntity):

    Dbid: float64
    SnapTime: datetime
    SnapId: float64
    DbName: str
    FiletypeName: str
    Iops: float64
    Mbps: float64

    key_map = {
        'DBID': 'Dbid',
        'SNAP_TIME': 'SnapTime',
        'SNAP_ID': 'SnapId',
        'DB_NAME': 'DbName',
        'FILETYPE_NAME': 'FiletypeName',
        'IOPS': 'Iops',
        'MBPS': 'Mbps'
    }

    def __init__(self, **kwargs):
        """
        NonCdbIoFileTypeStatisticGlobal model, inheriting from BaseModel.

        Args:
            **kwargs: The kwargs for NonCdbIoFileTypeStatisticGlobal.
        """
        super().__init__(**kwargs)
