from base.domain.base_entity import BaseEntity
from datetime import datetime
from numpy import float64

class CdbPdbMetric(BaseEntity):

    SnapTime            : datetime
    DbName              : str
    InstanceName        : str
    PdbName             : str
    BkgdTPerS           : float64
    LReadsS             : float64
    ExecCountS          : float64
    HardPS              : float64
    SoftParseHit        : float64
    ParseFailedS        : float64
    SqlResTCs           : float64
    Aas                 : float64
    SeSess              : float64
    UserTranS           : float64
    DbWaitRatio         : float64
    NetTrafficMbS       : float64
    CommitsS            : float64
    WriteBks            : float64
    LogonsS             : float64
    WriteMbS            : float64
    DbBlockChangesS     : float64
    TotalParseS         : float64
    ExecWithoutParseHit : float64
    UserRollS           : float64
    CurrentCursorS      : float64
    DbCpuRatio          : float64
    PxSess              : float64
    RedoMbS             : float64
    SessTotal           : float64
    CpuPerS             : float64
    OpenCursorS         : float64
    LogonsTotal         : float64
    ReadBks             : float64
    ReadMbS             : float64
    UserCallS           : float64


    key_map = {
        'SNAP_TIME' : 'SnapTime',
        'DB_NAME' : 'DbName',
        'INSTANCE_NAME' : 'InstanceName',
        'PDB_NAME' : 'PdbName',
        'BKGD_T_PER_S' : 'BkgdTPerS',
        'L_READS_S' : 'LReadsS',
        'EXEC_COUNT_S' : 'ExecCountS',
        'HARD_P_S' : 'HardPS',
        'SOFT_PARSE_HIT' : 'SoftParseHit',
        'PARSE_FAILED_S' : 'ParseFailedS',
        'SQL_RES_T_CS' : 'SqlResTCs',
        'AAS' : 'Aas',
        'SE_SESS' : 'SeSess',
        'USER_TRAN_S' : 'UserTranS',
        'DB_WAIT_RATIO' : 'DbWaitRatio',
        'NET_TRAFFIC_MB_S' : 'NetTrafficMbS',
        'COMMITS_S' : 'CommitsS',
        'WRITE_BKS' : 'WriteBks',
        'LOGONS_S' : 'LogonsS',
        'WRITE_MB_S' : 'WriteMbS',
        'DB_BLOCK_CHANGES_S' : 'DbBlockChangesS',
        'TOTAL_PARSE_S' : 'TotalParseS',
        'EXEC_WITHOUT_PARSE_HIT' : 'ExecWithoutParseHit',
        'USER_ROLL_S' : 'UserRollS',
        'CURRENT_CURSOR_S' : 'CurrentCursorS',
        'DB_CPU_RATIO' : 'DbCpuRatio',
        'PX_SESS' : 'PxSess',
        'REDO_MB_S' : 'RedoMbS',
        'SESS_TOTAL' : 'SessTotal',
        'CPU_PER_S' : 'CpuPerS',
        'OPEN_CURSOR_S' : 'OpenCursorS',
        'LOGONS_TOTAL' : 'LogonsTotal',
        'READ_BKS' : 'ReadBks',
        'READ_MB_S' : 'ReadMbS',
        'USER_CALL_S' : 'UserCallS'
    }

    def __init__(self, **kwargs):
        """
        CdbPdbMetric model, inheriting from BaseModel.

        Args:
            **kwargs: The kwargs for CdbPdbMetric.
        """
        super().__init__(**kwargs)
