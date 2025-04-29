from base.domain.base_entity import BaseEntity
from datetime import datetime
from numpy import float64

class OdbAshCpuWaitAnalysicReport(BaseEntity):

    DbName: str
    InstanceName: str
    SnapId: float64
    Endtime: datetime
    SampleCount: float64
    SessionCount: float64    
    Aas: float64
    AasPerCpu: float64
    OnCpu: float64
    Waiting: float64
    WaitingPct: float64

    key_map = {
        'DB_NAME': 'DbName',
        'INSTANCE_NAME': 'InstanceName',        
        'SNAP_ID': 'SnapId',
        'ENDTIME': 'Endtime',
        'SAMPLE_COUNT': 'SampleCount',
        'SESSION_COUNT': 'SessionCount',        
        'AAS': 'Aas',
        'AAS_PER_CPU': 'AasPerCpu',
        'ON_CPU': 'OnCpu',
        'WAITING': 'Waiting',
        'WAITING_PCT': 'WaitingPct'
    }

    def __init__(self, **kwargs):
        """
        OdbAshCpuWaitAnalysicReport model, inheriting from BaseModel.

        Args:
            **kwargs: The kwargs for OdbAshCpuWaitAnalysicReport.
        """
        super().__init__(**kwargs)

