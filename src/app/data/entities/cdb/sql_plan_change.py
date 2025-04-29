from base.domain.base_entity import BaseEntity
from datetime import datetime
from numpy import float64

class CdbSqlPlanChange(BaseEntity):

    PdbName: str
    SqlId: str
    Plans: float64
    PlanHashValue: float64
    MinTime: str
    MaxTime: str
    MedSecsPerExec: float64
    Executions: float64
    AproxTotSecs: float64
    StdSecs: float64
    AvgSecs: float64
    MinSecs: float64
    MaxSecs: float64

    key_map = {
        'PDB_NAME': 'PdbName',
        'SQL_ID': 'SqlId',
        'PLANS': 'Plans',
        'PLAN_HASH_VALUE': 'PlanHashValue',
        'MIN_TIME': 'MinTime',
        'MAX_TIME': 'MaxTime',
        'MED_SECS_PER_EXEC': 'MedSecsPerExec',
        'EXECUTIONS': 'Executions',
        'APROX_TOT_SECS': 'AproxTotSecs',
        'STD_SECS': 'StdSecs',
        'AVG_SECS': 'AvgSecs',
        'MIN_SECS': 'MinSecs',
        'MAX_SECS': 'MaxSecs'
    }

    def __init__(self, **kwargs):
        """
        CdbSqlPlanChange model, inheriting from BaseModel.

        Args:
            **kwargs: The kwargs for CdbSqlPlanChange.
        """
        super().__init__(**kwargs)

    