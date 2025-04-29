from base.domain.base_entity import BaseEntity
from datetime import datetime
from numpy import float64

class OdbOsStatistic(BaseEntity):

    DbName: str
    InstanceName: str
    SnapTime: datetime
    NumCpus: float64
    NumCores: float64
    NumSocks: float64
    BeginLoad: float64
    EndLoad: float64
    PctBusy: float64
    PctUser: float64
    PctSys: float64
    PctWio: float64
    PctIdl: float64
    BusyTime: float64
    IdleTime: float64
    TotalTime: float64
    HostCpu: float64
    NiceTime: object
    RsCpuWaitTime: float64
    Vmin: float64
    Vmout: float64
    MemB: float64
    MemFree: object
    MemUnactive: object
    Swap: object
    OsCpuWaitTime: float64

    key_map = {
        'DB_NAME': 'DbName',
        'INSTANCE_NAME': 'InstanceName',
        'SNAP_TIME': 'SnapTime',
        'NUM_CPUS': 'NumCpus',
        'NUM_CORES': 'NumCores',
        'NUM_SOCKS': 'NumSocks',
        'BEGIN_LOAD': 'BeginLoad',
        'END_LOAD': 'EndLoad',
        'PCT_BUSY': 'PctBusy',
        'PCT_USER': 'PctUser',
        'PCT_SYS': 'PctSys',
        'PCT_WIO': 'PctWio',
        'PCT_IDL': 'PctIdl',
        'BUSY_TIME': 'BusyTime',
        'IDLE_TIME': 'IdleTime',
        'TOTAL_TIME': 'TotalTime',
        'HOST_CPU': 'HostCpu',
        'NICE_TIME': 'NiceTime',
        'RS_CPU_WAIT_TIME': 'RsCpuWaitTime',
        'VMIN': 'Vmin',
        'VMOUT': 'Vmout',
        'MEM_B': 'MemB',
        'MEM_FREE': 'MemFree',
        'MEM_UNACTIVE': 'MemUnactive',
        'SWAP': 'Swap',
        'OS_CPU_WAIT_TIME': 'OsCpuWaitTime'
    }

    def __init__(self, **kwargs):
        """
        OdbOsStatistic model, inheriting from BaseModel.

        Args:
            **kwargs: The kwargs for OdbOsStatistic.
        """
        super().__init__(**kwargs)
