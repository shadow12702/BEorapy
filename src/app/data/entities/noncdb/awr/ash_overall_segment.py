from base.domain.base_entity import BaseEntity
from numpy import float64

class NonCdbAwrAshOverallSegment(BaseEntity):

    DbName: str
    InstanceName: str
    Owner: str
    ObjectName: str
    Pct: float64

    key_map = {
        'DB_NAME': 'DbName',
        'INSTANCE_NAME': 'InstanceName',
        'OWNER': 'Owner',
        'OBJECT_NAME': 'ObjectName',
        'PCT': 'Pct'
    }

    def __init__(self, **kwargs):
        """
        NonCdbAwrAshOverallSegment model, inheriting from BaseModel.

        Args:
            **kwargs: The kwargs for NonCdbAwrAshOverallSegment.
        """
        super().__init__(**kwargs)
