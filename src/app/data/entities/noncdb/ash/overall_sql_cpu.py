from base.domain.base_entity import BaseEntity

from numpy import float64

class NonCdbAshOverallSqlCpu(BaseEntity):

    DbName: str
    InstanceName: str
    SqlId: str
    Pct: float64
    SqlText: str

    key_map = {
        'DB_NAME': 'DbName',
        'INSTANCE_NAME': 'InstanceName',
        'SQL_ID': 'SqlId',
        'PCT': 'Pct',
        'SQL_TEXT': 'SqlText'
    }

    def __init__(self, **kwargs):
        """
        NonCdbAshOverallSqlCpu model, inheriting from BaseModel.

        Args:
            **kwargs: The kwargs for NonCdbAshOverallSqlCpu.
        """
        super().__init__(**kwargs)
