from base.domain.base_entity import BaseEntity
from datetime import datetime
from numpy import float64

class OdbTimeModelStatistic(BaseEntity):

    DbName        : str
    InstanceName  : str
    SnapTime      : datetime
    SnapId        : float64
    DbTime        : float64
    DbCpu         : float64
    SqlexecTime   : float64
    ParseTime     : float64
    HparseTime    : float64
    PlsqlTime     : float64
    PlsqlComp     : float64
    PlsqlInb      : float64
    JavaTime      : float64
    FparseTime    : float64
    ConTime       : float64
    BgTime        : float64
    BgCpu         : float64
    CpuPctDbt     : float64
    SqlPctDbt     : float64
    ParsePctDbt   : float64
    HparsePctDbt  : float64
    PlsqlPctDbt   : float64
    FparsePctDbt  : float64
    JavaPctDbt    : float64
    ConPctDbt     : float64
    BgtPctTbgt    : float64
    BgCpuPctDbt   : float64


    key_map = {
        'DB_NAME' : 'DbName',
        'INSTANCE_NAME' : 'InstanceName',
        'SNAP_TIME' : 'SnapTime',
        'SNAP_ID' : 'SnapId',
        'DB_TIME' : 'DbTime',
        'DB_CPU' : 'DbCpu',
        'SQLEXEC_TIME' : 'SqlexecTime',
        'PARSE_TIME' : 'ParseTime',
        'HPARSE_TIME' : 'HparseTime',
        'PLSQL_TIME' : 'PlsqlTime',
        'PLSQL_COMP' : 'PlsqlComp',
        'PLSQL_INB' : 'PlsqlInb',
        'JAVA_TIME' : 'JavaTime',
        'FPARSE_TIME' : 'FparseTime',
        'CON_TIME' : 'ConTime',
        'BG_TIME' : 'BgTime',
        'BG_CPU' : 'BgCpu',
        'CPU_PCT_DBT' : 'CpuPctDbt',
        'SQL_PCT_DBT' : 'SqlPctDbt',
        'PARSE_PCT_DBT' : 'ParsePctDbt',
        'HPARSE_PCT_DBT' : 'HparsePctDbt',
        'PLSQL_PCT_DBT' : 'PlsqlPctDbt',
        'FPARSE_PCT_DBT' : 'FparsePctDbt',
        'JAVA_PCT_DBT' : 'JavaPctDbt',
        'CON_PCT_DBT' : 'ConPctDbt',
        'BGT_PCT_TBGT' : 'BgtPctTbgt',
        'BG_CPU_PCT_DBT' : 'BgCpuPctDbt'
    }

    def __init__(self, **kwargs):
        """
        OdbTimeModelStatistic model, inheriting from BaseModel.

        Args:
            **kwargs: The kwargs for OdbTimeModelStatistic.
        """
        super().__init__(**kwargs)
