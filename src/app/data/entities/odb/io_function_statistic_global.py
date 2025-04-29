from base.domain.base_entity import BaseEntity
from datetime import datetime
from numpy import float64

class OdbIoFunctionStatisticGlobal(BaseEntity):

    Dbid: float64
    SnapTime: datetime
    SnapId: float64
    DbName: str
    FunctionName: str
    ReadReqs: object
    WriteReqs: object
    ReadMb: object
    WriteMb: object

    key_map = {
        'DBID': 'Dbid',
        'SNAP_TIME': 'SnapTime',
        'SNAP_ID': 'SnapId',
        'DB_NAME': 'DbName',
        'FUNCTION_NAME': 'FunctionName',
        'READ_REQS': 'ReadReqs',
        'WRITE_REQS': 'WriteReqs',
        'READ_MB': 'ReadMb',
        'WRITE_MB': 'WriteMb'
    }

    def __init__(self, **kwargs):
        """
        OdbIoFunctionStatisticGlobal model, inheriting from BaseModel.

        Args:
            **kwargs: The kwargs for OdbIoFunctionStatisticGlobal.
        """
        super().__init__(**kwargs)
