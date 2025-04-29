from base.domain.base_entity import BaseEntity
from datetime import datetime
from numpy import float64

class OdbIoFunctionStatistic(BaseEntity):

    DbName: str
    InstanceName: str
    SnapId: float64
    SnapTime: datetime
    FunctionName: str
    Mbps: object
    Iops: object
    Waits: object
    Avgtime: object

    key_map = {
        'DB_NAME': 'DbName',
        'INSTANCE_NAME': 'InstanceName',
        'SNAP_ID': 'SnapId',
        'SNAP_TIME': 'SnapTime',
        'FUNCTION_NAME': 'FunctionName',
        'MBPS': 'Mbps',
        'IOPS': 'Iops',
        'WAITS': 'Waits',
        'AVGTIME': 'Avgtime'
    }

    def __init__(self, **kwargs):
        """
        OdbIoFunctionStatistic model, inheriting from BaseModel.

        Args:
            **kwargs: The kwargs for OdbIoFunctionStatistic.
        """
        super().__init__(**kwargs)
