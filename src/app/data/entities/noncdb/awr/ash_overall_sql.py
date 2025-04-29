from base.domain.base_entity import BaseEntity
from numpy import float64

class NonCdbAwrAshOverallSql(BaseEntity):

    DbName: str
    InstanceName: str
    SqlId: str
    Pct: float64

    key_map = {
        'DB_NAME': 'DbName',
        'INSTANCE_NAME': 'InstanceName',
        'SQL_ID': 'SqlId',
        'PCT': 'Pct'
    }

    def __init__(self, **kwargs):
        """
        NonCdbAwrAshOverallSql model, inheriting from BaseModel.

        Args:
            **kwargs: The kwargs for NonCdbAwrAshOverallSql.
        """
        super().__init__(**kwargs)
