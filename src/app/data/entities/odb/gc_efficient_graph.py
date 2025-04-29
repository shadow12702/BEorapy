from base.domain.base_entity import BaseEntity
from datetime import datetime
from numpy import float64

class OdbGcEfficientGraph(BaseEntity):

    DbName: str
    InstanceName: str
    SnapId: float64
    Dbid: float64
    SnapTime: datetime
    Lc: object
    Rc: object
    Dsk: object

    key_map = {
        'DB_NAME': 'DbName',
        'INSTANCE_NAME': 'InstanceName',
        'SNAP_ID': 'SnapId',
        'DBID': 'Dbid',
        'SNAP_TIME': 'SnapTime',
        'LC': 'Lc',
        'RC': 'Rc',
        'DSK': 'Dsk'
    }

    def __init__(self, **kwargs):
        """
        OdbGcEfficientGraph model, inheriting from BaseModel.

        Args:
            **kwargs: The kwargs for OdbGcEfficientGraph.
        """
        super().__init__(**kwargs)
