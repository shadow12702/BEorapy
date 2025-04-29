from base.domain.base_entity import BaseEntity
from numpy import float64

class NonCdbAshOverallSqlEvent(BaseEntity):

    DbName: str
    InstanceName: str
    SqlId: str
    Event: str
    TimeMs: object
    Pct: float64
    SqlText: str

    key_map = {
        'INSTANCE_NAME': 'InstanceName',
        'DB_NAME': 'DbName',
        'SQL_ID': 'SqlId',
        'EVENT': 'Event',
        'TIME_MS': 'TimeMs',
        'PCT': 'Pct',
        'SQL_TEXT': 'SqlText'
    }

    def __init__(self, **kwargs):
        """
        NonCdbAshOverallSqlEvent model, inheriting from BaseModel.

        Args:
            **kwargs: The kwargs for NonCdbAshOverallSqlEvent.
        """
        super().__init__(**kwargs)
