from base.domain.base_entity import BaseEntity
from datetime import datetime
from numpy import float64

class OdbExaDatabaseSystat(BaseEntity):

    DbName: str
    InstanceName: str
    SnapId: float64
    SnapTime: datetime
    PhysicalReadIops: float64
    PhysicalWriteIops: float64
    FlashCacheIops: float64
    PhysicalReadMb: float64
    Incon: float64
    StorageSave: float64
    CellOffLoad: float64
    CellReturn: float64
    UncompressMb: float64
    PassthruQuaMb: float64
    PassthruOffLoadMb: float64
    PhysicalByteAddSmMb: float64
    EligibleSmMb: float64
    PhysicalByteCcSavedMb: float64
    PhysicalByteFileCreateSavedMb: float64
    PhysicalByteRmanRestoreSavedMb: float64
    PhysicalByteBackToDbMb: float64
    FlashHitRatio: float64
    SmartScanEligibilityRatio: float64
    StorageIdxRatio: float64
    SmartScanEfficiencyRatio: float64
    RbmaRead: float64
    RbmaWrite: float64
    PmemReadIops: float64
    PmemWriteIops: float64

    key_map = {
        'DB_NAME': 'DbName',
        'INSTANCE_NAME': 'InstanceName',
        'SNAP_ID': 'SnapId',
        'SNAP_TIME': 'SnapTime',
        'PHYREAD_IOPS': 'PhysicalReadIops',
        'PHYWRT_IOPS': 'PhysicalWriteIops',
        'FLASHCACH_IOPS': 'FlashCacheIops',
        'PHYREAD_MB': 'PhysicalReadMb',
        'INCON': 'Incon',
        'STORAGESAVE': 'StorageSave',
        'CELL_OFFLOAD': 'CellOffLoad',
        'CELL_RETURN': 'CellReturn',
        'UNCOMPRESS_MB': 'UncompressMb',
        'PASSTHRU_QUA_MB': 'PassthruQuaMb',
        'PASSTHRU_OFFLOAD_MB': 'PassthruOffLoadMb',
        'PHYBYTE_ADD_SM_MB': 'PhysicalByteAddSmMb',
        'ELIGIBLE_SM_MB': 'EligibleSmMb',
        'PHYBYTE_CCSAVED_MB': 'PhysicalByteCcSavedMb',
        'PHYBYTE_FILECREATESAVED_MB': 'PhysicalByteFileCreateSavedMb',
        'PHYBYTE_RMANRESTORESAVED_MB': 'PhysicalByteRmanRestoreSavedMb',
        'PHYBYTE_BACKTODB_MB': 'PhysicalByteBackToDbMb',
        'FLASHHIT_RATIO': 'FlashHitRatio',
        'SMARTSCAN_ELIGIBILITY_RATIO': 'SmartScanEligibilityRatio',
        'STORAGEIDX_RATIO': 'StorageIdxRatio',
        'SMARTSCAN_EFFICIENCY_RATIO': 'SmartScanEfficiencyRatio',
        'RBMAREAD': 'RbmaRead',
        'RBMAWRITE': 'RbmaWrite',
        'PMEM_READ_IOPS': 'PmemReadIops',
        'PMEM_WRITE_IOPS': 'PmemWriteIops'
    }

    def __init__(self, **kwargs):
        """
        OdbExaDatabaseSystat model, inheriting from BaseModel.

        Args:
            **kwargs: The kwargs for OdbExaDatabaseSystat.
        """
        super().__init__(**kwargs)
