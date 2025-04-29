from base.domain.base_entity import BaseEntity
from datetime import datetime
from numpy import float64

class OdbExaCellServerIoStatisticCell(BaseEntity):

    SnapTime: datetime
    CellName: str
    DiskUltil: object
    IoRequestsAvg: float64
    IoMbAvg: float64
    SmallReadsAvg: float64
    SmallWritesAvg: float64
    LargeReadsAvg: float64
    LargeWritesAvg: float64
    SmallReadBytesAvg: float64
    SmallWriteBytesAvg: float64
    LargeReadBytesAvg: float64
    LargeWriteBytesAvg: float64
    SmallReadLatencyAvg: float64
    SmallWriteLatencyAvg: float64
    LargeReadLatencyAvg: float64
    LargeWriteLatencyAvg: float64
    AppIoRequestsAvg: float64
    AppIoBytesAvg: float64
    AppIoLatencyAvg: float64

    key_map = {
        'SNAP_TIME': 'SnapTime',
        'CELL_NAME': 'CellName',
        'DISK_ULTIL': 'DiskUltil',
        'IO_REQUESTS_AVG': 'IoRequestsAvg',
        'IO_MB_AVG': 'IoMbAvg',
        'SMALL_READS_AVG': 'SmallReadsAvg',
        'SMALL_WRITES_AVG': 'SmallWritesAvg',
        'LARGE_READS_AVG': 'LargeReadsAvg',
        'LARGE_WRITES_AVG': 'LargeWritesAvg',
        'SMALL_READ_BYTES_AVG': 'SmallReadBytesAvg',
        'SMALL_WRITE_BYTES_AVG': 'SmallWriteBytesAvg',
        'LARGE_READ_BYTES_AVG': 'LargeReadBytesAvg',
        'LARGE_WRITE_BYTES_AVG': 'LargeWriteBytesAvg',
        'SMALL_READ_LATENCY_AVG': 'SmallReadLatencyAvg',
        'SMALL_WRITE_LATENCY_AVG': 'SmallWriteLatencyAvg',
        'LARGE_READ_LATENCY_AVG': 'LargeReadLatencyAvg',
        'LARGE_WRITE_LATENCY_AVG': 'LargeWriteLatencyAvg',
        'APP_IO_REQUESTS_AVG': 'AppIoRequestsAvg',
        'APP_IO_BYTES_AVG': 'AppIoBytesAvg',
        'APP_IO_LATENCY_AVG': 'AppIoLatencyAvg'
    }

    def __init__(self, **kwargs):
        """
        ExaCellServerIoStatisticCell model, inheriting from BaseModel.

        Args:
            **kwargs: The kwargs for ExaCellServerIoStatisticCell.
        """
        super().__init__(**kwargs)
