from base.domain.base_entity import BaseEntity
from datetime import datetime
from numpy import float64

class OdbAshOverallSqlOperation(BaseEntity):

    DbName: str
    InstanceName: str
    Operation: float64
    Pct: float64

    key_map = {
        'INSTANCE_NAME': 'InstanceName',
        'DB_NAME': 'DbName',
        'OPERATION': 'Operation',
        'PCT': 'Pct'
    }

    def __init__(self, **kwargs):
        """
        OdbAshOverallSqlOperation model, inheriting from BaseModel.

        Args:
            **kwargs: The kwargs for OdbAshOverallSqlOperation.
        """
        super().__init__(**kwargs)
