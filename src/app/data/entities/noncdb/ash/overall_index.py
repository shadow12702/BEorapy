from base.domain.base_entity import BaseEntity
from datetime import datetime
from numpy import float64

class NonCdbAshOverallIndex(BaseEntity):

    DbName: str
    InstanceName: str
    ObjectName: str
    TimeMs: datetime
    Pct: float64

    key_map = {
        'INSTANCE_NAME': 'InstanceName',
        'DB_NAME': 'DbName',
        'OBJECT_NAME': 'ObjectName',
        'TIME_MS': 'TimeMs',
        'PCT': 'Pct'
    }

    def __init__(self, **kwargs):
        """
        NonCdbAshOverallIndex model, inheriting from BaseModel.

        Args:
            **kwargs: The kwargs for NonCdbAshOverallIndex.
        """
        super().__init__(**kwargs)
