from base.domain.base_entity import BaseEntity
from numpy import float64

class NonCdbSqlPlanChange(BaseEntity):

    SqlId: str
    Plans: float64
    PlanHashValue: float64
    MinTime: str
    MaxTime: str
    MedSecs: float64
    Executions: float64
    AproxTotSecs: float64
    StdSecs: float64
    AvgSecs: float64
    MinSecs: float64
    MaxSecs: float64

    key_map = {
        'SQL_ID': 'SqlId',
        'PLANS': 'Plans',
        'PLAN_HASH_VALUE': 'PlanHashValue',
        'MIN_TIME': 'MinTime',
        'MAX_TIME': 'MaxTime',
        'MED_SECS': 'MedSecs',
        'EXECUTIONS': 'Executions',
        'APROX_TOT_SECS': 'AproxTotSecs',
        'STD_SECS': 'StdSecs',
        'AVG_SECS': 'AvgSecs',
        'MIN_SECS': 'MinSecs',
        'MAX_SECS': 'MaxSecs'
    }

    def __init__(self, **kwargs):
        """
        NonCdbSqlPlanChange model, inheriting from BaseModel.

        Args:
            **kwargs: The kwargs for NonCdbSqlPlanChange.
        """
        super().__init__(**kwargs)
