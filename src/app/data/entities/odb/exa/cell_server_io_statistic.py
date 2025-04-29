
from app.data.entities.odb.exa.cell_server_io_statistic_cell import OdbExaCellServerIoStatisticCell

class OdbExaCellServerIoStatistic(OdbExaCellServerIoStatisticCell):

    Disk: object
    DiskName: str
    
    key_map = {
        'DISK': 'Disk',
        'DISK_NAME': 'DiskName',
        **OdbExaCellServerIoStatisticCell.key_map
    }

    def __init__(self, **kwargs):
        """
        OdbExaCellServerIoStatistic model, inheriting from BaseModel.

        Args:
            **kwargs: The kwargs for OdbExaCellServerIoStatistic.
        """
        super().__init__(**kwargs)
