from base.domain.base_entity import BaseEntity
from numpy import float64

class NonCdbAshOverallTable(BaseEntity):

    InstanceName: str
    DbName: str
    ObjectName: str
    TimeMs: object
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
        NonCdbAshOverallTable model, inheriting from BaseModel.

        Args:
            **kwargs: The kwargs for NonCdbAshOverallTable.
        """
        super().__init__(**kwargs)
