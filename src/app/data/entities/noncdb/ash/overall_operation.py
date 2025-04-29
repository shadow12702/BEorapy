from base.domain.base_entity import BaseEntity
from datetime import datetime
from numpy import float64

class NonCdbAshOverallOperation(BaseEntity):

    DbName: str
    InstanceName: str
    SqlPlanOperation: object
    Pct: float64

    key_map = {
        'DB_NAME': 'DbName',
        'INSTANCE_NAME': 'InstanceName',
        'SQL_PLAN_OPERATION': 'SqlPlanOperation',
        'PCT': 'Pct'
    }

    def __init__(self, **kwargs):
        """
        NonCdbAshOverallOperation model, inheriting from BaseModel.

        Args:
            **kwargs: The kwargs for NonCdbAshOverallOperation.
        """
        super().__init__(**kwargs)
