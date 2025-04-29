from base.domain.base_entity import BaseEntity
from datetime import datetime
from numpy import float64

class OdbExaTopDatabaseIoStatistic(BaseEntity):

    EndSnapId: float64
    CellName: str
    SnapTime: datetime
    SrcDbName: str
    DiskRequests: float64
    FlashRequests: float64
    DiskMb: float64
    FlashMb: float64
    DiskSmallRequests: float64
    FlashSmallRequests: float64
    DiskLargeRequests: float64
    FlashLargeRequests: float64
    DiskSmallSvt: float64
    DiskLargeSvt: float64
    FlashSmallSvt: float64
    FlashLargeSvt: float64
    DiskSmallIoQueue: float64
    DiskLargeIoQueue: float64
    FlashSmallIoQueue: float64
    FlashLargeIoQueue: float64

    key_map = {
        'END_SNAP_ID': 'EndSnapId',
        'CELL_NAME': 'CellName',
        'SNAP_TIME': 'SnapTime',
        'SRC_DBNAME': 'SrcDbName',
        'DISK_REQUESTS': 'DiskRequests',
        'FLASH_REQUESTS': 'FlashRequests',
        'DISKMB': 'DiskMb',
        'FLASHMB': 'FlashMb',
        'DISK_SMALL_REQUESTS': 'DiskSmallRequests',
        'FLASH_SMALL_REQUESTS': 'FlashSmallRequests',
        'DISK_LARGE_REQUESTS': 'DiskLargeRequests',
        'FLASH_LARGE_REQUESTS': 'FlashLargeRequests',
        'DISK_SMALL_SVT': 'DiskSmallSvt',
        'DISK_LARGE_SVT': 'DiskLargeSvt',
        'FLASH_SMALL_SVT': 'FlashSmallSvt',
        'FLASH_LARGE_SVT': 'FlashLargeSvt',
        'DISK_SMALL_IOQUEUE': 'DiskSmallIoQueue',
        'DISK_LARGE_IOQUEUE': 'DiskLargeIoQueue',
        'FLASH_SMALL_IOQUEUE': 'FlashSmallIoQueue',
        'FLASH_LARGE_IOQUEUE': 'FlashLargeIoQueue'
    }

    def __init__(self, **kwargs):
        """
        OdbExaTopDatabaseIoStatistic model, inheriting from BaseModel.

        Args:
            **kwargs: The kwargs for OdbExaTopDatabaseIoStatistic.
        """
        super().__init__(**kwargs)
