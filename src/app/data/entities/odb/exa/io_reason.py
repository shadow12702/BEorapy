from base.domain.base_entity import BaseEntity
from datetime import datetime
from numpy import float64

class OdbExaIoReason(BaseEntity):

    EndSnapId: float64
    CellName: str
    SnapTime: datetime
    ReasonName: str
    Iops: object
    Mb: object

    key_map = {
        'END_SNAP_ID': 'EndSnapId',
        'CELL_NAME': 'CellName',
        'SNAP_TIME': 'SnapTime',
        'REASON_NAME': 'ReasonName',
        'IOPS': 'Iops',
        'MB': 'Mb'
    }

    def __init__(self, **kwargs):
        """
        OdbExaIoReason model, inheriting from BaseModel.

        Args:
            **kwargs: The kwargs for OdbExaIoReason.
        """
        super().__init__(**kwargs)
