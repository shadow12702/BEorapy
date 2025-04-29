from base.domain.base_entity import BaseEntity
from numpy import float64

class NonCdbAwrAshOverallEvent(BaseEntity):

    DbName: str
    InstanceName: str
    Event: str
    Pct: float64

    key_map = {
        'DB_NAME': 'DbName',
        'INSTANCE_NAME': 'InstanceName',
        'EVENT': 'Event',
        'PCT': 'Pct'
    }

    def __init__(self, **kwargs):
        """
        NonCdbAwrAshOverallEvent model, inheriting from BaseModel.

        Args:
            **kwargs: The kwargs for NonCdbAwrAshOverallEvent.
        """
        super().__init__(**kwargs)
