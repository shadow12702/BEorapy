from base.domain.base_entity import BaseEntity
from datetime import datetime
from numpy import float64

class OdbExaCellAlert(BaseEntity):

    SnapId: float64
    SnapTime: datetime
    CellName: str
    Critical: float64
    Warning: float64
    Info: float64

    key_map = {
        'SNAP_ID': 'SnapId',
        'SNAP_TIME': 'SnapTime',
        'CELL_NAME': 'CellName',
        'CRITICAL': 'Critical',
        'WARNING': 'Warning',
        'INFO': 'Info'
    }

    def __init__(self, **kwargs):
        """
        OdbExaCellAlert model, inheriting from BaseModel.

        Args:
            **kwargs: The kwargs for OdbExaCellAlert.
        """
        super().__init__(**kwargs)
