from base.domain.base_entity import BaseEntity
from datetime import datetime
from numpy import float64

class OdbDbaHistoryStatisticGlobal(BaseEntity):

    Dbid: float64
    SnapTime: datetime
    SnapId: float64
    DbName: str
    PhysicalWrite: float64
    PhysicalWriteMb: float64
    PhysicalRead: float64
    PhysicalReadMb: float64
    PhysicalReadOpt: float64
    PhysicalWriteOpt: float64
    PhysicalReadOptMb: float64
    PhysicalWriteOptMb: float64
    PhysicalReadMul: float64
    PhysicalWriteMul: float64
    RedoMb: float64
    Redo: float64
    LogCal: float64
    LogCur: float64
    Slg: float64
    Blc: float64
    Pt: float64
    Ph: float64
    Pf: float64
    Ucom: float64
    Crl: float64
    TnxRoll: float64
    Uroll: float64
    Ucall: float64
    ExecCount: float64

    key_map = {
        'DBID': 'Dbid',
        'SNAP_TIME': 'SnapTime',
        'SNAP_ID': 'SnapId',
        'DB_NAME': 'DbName',
        'PHYWRITE': 'PhysicalWrite',
        'PHYWRITE_MB': 'PhysicalWriteMb',
        'PHYREAD': 'PhysicalRead',
        'PHYREAD_MB': 'PhysicalReadMb',
        'PHYREAD_OPT': 'PhysicalReadOpt',
        'PHYWRITE_OPT': 'PhysicalWriteOpt',
        'PHYREAD_OPT_MB': 'PhysicalReadOptMb',
        'PHYWRITE_OPT_MB': 'PhysicalWriteOptMb',
        'PHYREAD_MUL': 'PhysicalReadMul',
        'PHYWRITE_MUL': 'PhysicalWriteMul',
        'REDO_MB': 'RedoMb',
        'REDO': 'Redo',
        'LOG_CAL': 'LogCal',
        'LOG_CUR': 'LogCur',
        'SLG': 'Slg',
        'BLC': 'Blc',
        'PT': 'Pt',
        'PH': 'Ph',
        'PF': 'Pf',
        'UCOM': 'Ucom',
        'CRL': 'Crl',
        'TNXROLL': 'TnxRoll',
        'UROLL': 'Uroll',
        'UCALL': 'Ucall',
        'EXECCNT': 'ExecCount'
    }

    def __init__(self, **kwargs):
        """
        OdbDbaHistoryStatisticGlobal model, inheriting from BaseModel.

        Args:
            **kwargs: The kwargs for OdbDbaHistoryStatisticGlobal.
        """
        super().__init__(**kwargs)
