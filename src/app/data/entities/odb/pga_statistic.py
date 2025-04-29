from base.domain.base_entity import BaseEntity
from datetime import datetime
from numpy import float64

class OdbPgaStatistic(BaseEntity):

    DbName: str
    InstanceName: str
    SnapId: float64
    SnapTime: datetime
    PgaMemFreedToOs: float64
    AggrPgaAutoTarget: float64
    AggrPgaTargetParam: float64
    BytesProcessed: float64
    ExtraBytesRw: float64
    GlobalMemoryBound: float64
    MaxPgaAllocated: float64
    MaxPgaUsedAutWa: float64
    MaxPgaUsedManWa: float64
    TotPgaAllocated: float64
    TotPgaInuse: float64
    TotPgaUsedAutWa: float64
    TotPgaUsedManWa: float64
    TotFreeablePgaMem: float64
    CacheHit: float64

    key_map = {
        'DB_NAME': 'DbName',
        'INSTANCE_NAME': 'InstanceName',
        'SNAP_ID': 'SnapId',
        'SNAP_TIME': 'SnapTime',
        'PGA_MEM_FREED_TO_OS': 'PgaMemFreedToOs',
        'AGGR_PGA_AUTO_TARGET': 'AggrPgaAutoTarget',
        'AGGR_PGA_TARGET_PARAM': 'AggrPgaTargetParam',
        'BYTES_PROCESSED': 'BytesProcessed',
        'EXTRA_BYTES_RW': 'ExtraBytesRw',
        'GLOBAL_MEMORY_BOUND': 'GlobalMemoryBound',
        'MAX_PGA_ALLOCATED': 'MaxPgaAllocated',
        'MAX_PGA_USED_AUT_WA': 'MaxPgaUsedAutWa',
        'MAX_PGA_USED_MAN_WA': 'MaxPgaUsedManWa',
        'TOT_PGA_ALLOCATED': 'TotPgaAllocated',
        'TOT_PGA_INUSE': 'TotPgaInuse',
        'TOT_PGA_USED_AUT_WA': 'TotPgaUsedAutWa',
        'TOT_PGA_USED_MAN_WA': 'TotPgaUsedManWa',
        'TOT_FREEABLE_PGA_MEM': 'TotFreeablePgaMem',
        'CACHEHIT': 'CacheHit'
    }

    def __init__(self, **kwargs):
        """
        OdbPgaStatistic model, inheriting from BaseModel.

        Args:
            **kwargs: The kwargs for OdbPgaStatistic.
        """
        super().__init__(**kwargs)
