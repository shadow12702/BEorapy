from base.domain.base_entity import BaseEntity
from datetime import datetime

class OdbGcBlockSrvGraph(BaseEntity):

    DbName: str
    InstanceName: str
    SnapTime: datetime
    CrRequests: object
    CurrentRequests: object
    DataRequests: object
    UndoRequests: object
    TxRequests: object

    key_map = {
        'DB_NAME': 'DbName',
        'INSTANCE_NAME': 'InstanceName',
        'SNAP_TIME': 'SnapTime',
        'CR_REQUESTS': 'CrRequests',
        'CURRENT_REQUESTS': 'CurrentRequests',
        'DATA_REQUESTS': 'DataRequests',
        'UNDO_REQUESTS': 'UndoRequests',
        'TX_REQUESTS': 'TxRequests'
    }

    def __init__(self, **kwargs):
        """
        OdbGcBlockSrvGraph model, inheriting from BaseModel.

        Args:
            **kwargs: The kwargs for OdbGcBlockSrvGraph.
        """
        super().__init__(**kwargs)
