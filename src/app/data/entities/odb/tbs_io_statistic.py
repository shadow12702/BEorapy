from base.domain.base_entity import BaseEntity
from datetime import datetime
from numpy import float64

class OdbTbsIoStatistic(BaseEntity):

    DbName: str
    InstanceName: str
    SnapId: float64
    SnapTime: datetime
    Dur: float64
    Tsname: str
    Readtim: float64
    Reads: float64
    Rds: float64
    Atpr: float64
    Bpr: float64
    Writetim: float64
    Writes: float64
    Wrs: float64
    Atpw: float64
    Bpw: float64
    Waits: float64
    Atpwt: float64
    Ios: float64
    Iops: float64

    key_map = {
        'DB_NAME': 'DbName',
        'INSTANCE_NAME': 'InstanceName',
        'SNAP_ID': 'SnapId',
        'SNAP_TIME': 'SnapTime',
        'DUR': 'Dur',
        'TSNAME': 'Tsname',
        'READTIM': 'Readtim',
        'READS': 'Reads',
        'RDS': 'Rds',
        'ATPR': 'Atpr',
        'BPR': 'Bpr',
        'WRITETIM': 'Writetim',
        'WRITES': 'Writes',
        'WRS': 'Wrs',
        'ATPW': 'Atpw',
        'BPW': 'Bpw',
        'WAITS': 'Waits',
        'ATPWT': 'Atpwt',
        'IOS': 'Ios',
        'IOPS': 'Iops'
    }

    def __init__(self, **kwargs):
        """
        OdbTbsIoStatistic model, inheriting from BaseModel.

        Args:
            **kwargs: The kwargs for OdbTbsIoStatistic.
        """
        super().__init__(**kwargs)
