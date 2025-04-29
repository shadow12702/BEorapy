from base.domain.base_entity import BaseEntity
from datetime import datetime
from numpy import float64

class OdbAwrAasGraph(BaseEntity):

    InstanceName: str
    DbName: str
    SnapTime: datetime
    CpuCore: float64
    Aas: float64
    SnapId: float64

    key_map = {
        'DB_NAME': 'DbName',
        'INSTANCE_NAME': 'InstanceName',
        'SNAP_TIME': 'SnapTime',
        'CPUCORE': 'CpuCore',
        'AAS': 'Aas',
        'SNAP_ID': 'SnapId'
    }

    def __init__(self, **kwargs):
        """
        OdbAwrAasGraph model, inheriting from BaseModel.

        Args:
            **kwargs: The kwargs for OdbAwrAasGraph.
        """
        super().__init__(**kwargs)
