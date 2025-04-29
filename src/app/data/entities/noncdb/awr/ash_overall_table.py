from base.domain.base_entity import BaseEntity
from numpy import float64

class NonCdbAwrAshOverallTable(BaseEntity):

    DbName: str
    InstanceName: str
    ObjectName: str
    Pct: float64

    key_map = {
        'DB_NAME': 'DbName',
        'INSTANCE_NAME': 'InstanceName',
        'OBJECT_NAME': 'ObjectName',
        'PCT': 'Pct'
    }

    def __init__(self, **kwargs):
        """
        NonCdbAwrAshOverallTable model, inheriting from BaseModel.

        Args:
            **kwargs: The kwargs for NonCdbAwrAshOverallTable.
        """
        super().__init__(**kwargs)
