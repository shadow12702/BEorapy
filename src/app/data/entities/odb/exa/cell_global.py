from base.domain.base_entity import BaseEntity
from datetime import datetime
from numpy import float64

class OdbExaCellGlobal(BaseEntity):

    EndSnapId: float64
    SnapTime: datetime
    FlashCacheUsedMb: float64
    SmioPushBackPassthruMb: float64
    SmioPushBackHighCpuMb: float64
    SmioReadFlashCacheMb: float64
    SmioReadHardDiskMb: float64
    SmioSentBackDbMb: float64
    SmioTotalMb: float64
    StorageIdxSavedMb: float64
    TotalFlashReadMb: float64
    TotalFlashWriteMb: float64
    TotalFlashReadIops: float64
    TotalFlashWriteIops: float64
    RamCacheAllocatedMb: float64
    RamCacheReadMb: float64
    RamCacheReadMissMb: float64
    RamCacheFlashReadMissIops: float64
    RamCacheFlashReadIops: float64
    FlashLogRedoWriteDiskMb: float64
    FlashLogRedoWriteFlashMb: float64
    FlashAllocated: float64
    FlashReadMb: float64
    FlashScanReadMb: float64
    FlashColumnarReadMb: float64
    FlashUsedMb: float64
    FlashUsedOltpMb: float64
    FlashReadIops: float64
    FlashScanReadIops: float64
    FlashColumnarReadIops: float64
    PmemAllocated: float64
    PmemReadMb: float64
    PmemWriteMb: float64
    PmemWriteIops: float64
    PmemReadIops: float64
    PmemReadMissesIops: float64
    PmemInternalReadMb: float64
    PmemInternalReadIops: float64
    FlashCacheFistWriteIops: float64
    FlashCacheOverWriteIops: float64
    FlashCacheFistWriteMb: float64
    FlashCacheOverWriteMb: float64
    RedoLogWriteIops: float64
    RedoLogWriteLatency: float64
    IoCapCancelable: float64
    IoCapCanceled: float64
    IoCapUncancelable: float64

    key_map = {
        'END_SNAP_ID' : 'EndSnapId',
        'SNAP_TIME' : 'SnapTime',        
        'FLASHCACHEUSED_MB' : 'FlashCacheUsedMb',
        'SMIO_PUSHBACK_PASSTHRU_MB' : 'SmioPushBackPassthruMb',
        'SMIO_PUSHBACK_HIGHCPU_MB' : 'SmioPushBackHighCpuMb',
        'SMIO_READ_FLASHCACHE_MB' : 'SmioReadFlashCacheMb',
        'SMIO_READ_HARDDISK_MB' : 'SmioReadHardDiskMb',
        'SMIO_SENTBACK_DB_MB' : 'SmioSentBackDbMb',
        'SMIO_TOTAL_MB' : 'SmioTotalMb',
        'STORAGEIDX_SAVED_MB' : 'StorageIdxSavedMb',
        'TOTAL_FLASH_READ_MB' : 'TotalFlashReadMb',
        'TOTAL_FLASH_WRITE_MB' : 'TotalFlashWriteMb',
        'TOTAL_FLASH_READ_IOPS' : 'TotalFlashReadIops',
        'TOTAL_FLASH_WRITE_IOPS' : 'TotalFlashWriteIops',
        'RAMCACHE_ALLOCATED_MB' : 'RamCacheAllocatedMb',
        'RAMCACHE_READ_MB' : 'RamCacheReadMb',
        'RAMCACHE_READ_MISS_MB' : 'RamCacheReadMissMb',
        'RAMCACHE_FLASH_READ_MISS_IOPS' : 'RamCacheFlashReadMissIops',
        'RAMCACHE_FLASH_READ_IOPS' : 'RamCacheFlashReadIops',
        'FLASHLOG_REDOWRITE_DISK_MB' : 'FlashLogRedoWriteDiskMb',
        'FLASHLOG_REDOWRITE_FLASH_MB' : 'FlashLogRedoWriteFlashMb',
        'FLASH_ALLOCATED' : 'FlashAllocated',
        'FLASH_READ_MB' : 'FlashReadMb',
        'FLASH_SCAN_READ_MB' : 'FlashScanReadMb',
        'FLASH_COLUMNAR_READ_MB' : 'FlashColumnarReadMb',
        'FLASH_USED_MB' : 'FlashUsedMb',
        'FLASH_USED_OLTP_MB' : 'FlashUsedOltpMb',
        'FLASH_READ_IOPS' : 'FlashReadIops',
        'FLASH_SCAN_READ_IOPS' : 'FlashScanReadIops',
        'FLASH_COLUMNAR_READ_IOPS' : 'FlashColumnarReadIops',
        'PMEM_ALLOCATED' : 'PmemAllocated',
        'PMEM_READ_MB' : 'PmemReadMb',
        'PMEM_WRITE_MB' : 'PmemWriteMb',
        'PMEM_WRITE_IOPS' : 'PmemWriteIops',
        'PMEM_READ_IOPS' : 'PmemReadIops',
        'PMEM_READ_MISSES_IOPS' : 'PmemReadMissesIops',
        'PMEM_INTERNALREAD_MB' : 'PmemInternalReadMb',
        'PMEM_INTERNALREAD_IOPS' : 'PmemInternalReadIops',
        'FLASHCACHE_FISTWRITE_IOPS' : 'FlashCacheFistWriteIops',
        'FLASHCACHE_OVERWRITE_IOPS' : 'FlashCacheOverWriteIops',
        'FLASHCACHE_FISTWRITE_MB' : 'FlashCacheFistWriteMb',
        'FLASHCACHE_OVERWRITE_MB' : 'FlashCacheOverWriteMb',
        'REDOLOG_WRITE_IOPS' : 'RedoLogWriteIops',
        'REDOLOG_WRITE_LATENCY' : 'RedoLogWriteLatency',
        'IOCAP_CANCELABLE' : 'IoCapCancelable',
        'IOCAP_CANCELED' : 'IoCapCanceled',
        'IOCAP_UNCANCELABLE' : 'IoCapUncancelable'
    }

    def __init__(self, **kwargs):
        """
        OdbExaCellGlobal model, inheriting from BaseModel.

        Args:
            **kwargs: The kwargs for OdbExaCellGlobal.
        """
        super().__init__(**kwargs)
