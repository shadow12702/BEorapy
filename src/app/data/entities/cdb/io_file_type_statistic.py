from base.domain.base_entity import BaseEntity
from datetime import datetime
from numpy import float64

class CdbIoFileTypeStatistic(BaseEntity):

    DbName: str
    InstanceName: str
    PdbName: str
    SnapTime: datetime
    FiletypeName: str
    Mbps: float64
    Iops: float64

    key_map = {
        'DB_NAME': 'DbName',
        'INSTANCE_NAME': 'InstanceName',
        'PDB_NAME': 'PdbName',
        'SNAP_TIME': 'SnapTime',
        'FILETYPE_NAME': 'FiletypeName',
        'MBPS': 'Mbps',
        'IOPS': 'Iops'
    }

    def __init__(self, **kwargs):
        """
        CdbIoFileTypeStatistic model, inheriting from BaseModel.

        Args:
            **kwargs: The kwargs for CdbIoFileTypeStatistic.
        """
        super().__init__(**kwargs)
