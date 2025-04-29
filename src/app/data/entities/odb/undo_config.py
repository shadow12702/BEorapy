from base.domain.base_entity import BaseEntity
from datetime import datetime
from numpy import float64

class OdbUndoConfig(BaseEntity):

    DbName: str
    InstanceName: str
    SnapId: float64
    SnapTime: datetime
    UsedG: float64
    MaxQuery: float64
    TunedUndo: float64

    key_map = {
        'DB_NAME': 'DbName',
        'INSTANCE_NAME': 'InstanceName',
        'SNAP_ID': 'SnapId',
        'SNAP_TIME': 'SnapTime',
        'USED_G': 'UsedG',
        'MAXQUERY': 'MaxQuery',
        'TUNEDUNDO': 'TunedUndo'
    }

    def __init__(self, **kwargs):
        """
        OdbUndoConfig model, inheriting from BaseModel.

        Args:
            **kwargs: The kwargs for OdbUndoConfig.
        """
        super().__init__(**kwargs)
