from base.domain.base_entity import BaseEntity
from datetime import datetime
from numpy import float64

class NonCdbAshOverallEvent(BaseEntity):

    DbName: str
    InstanceName: str
    WaitClass: object
    Event: str
    Pct: float64

    key_map = {
        'INSTANCE_NAME': 'InstanceName',
        'DB_NAME': 'DbName',
        'WAIT_CLASS': 'WaitClass',
        'EVENT': 'Event',
        'PCT': 'Pct'
    }

    def __init__(self, **kwargs):
        """
        NonCdbAshOverallEvent model, inheriting from BaseModel.

        Args:
            **kwargs: The kwargs for NonCdbAshOverallEvent.
        """
        super().__init__(**kwargs)
