from base.domain.base_entity import BaseEntity
from numpy import float64

class NonCdbAwrAshOverallWaitClass(BaseEntity):

    DbName: str
    InstanceName: str
    WaitClass: object
    Pct: float64

    key_map = {
        'DB_NAME': 'DbName',
        'INSTANCE_NAME': 'InstanceName',
        'WAIT_CLASS': 'WaitClass',
        'PCT': 'Pct'
    }

    def __init__(self, **kwargs):
        """
        NonCdbAwrAshOverallWaitClass model, inheriting from BaseModel.

        Args:
            **kwargs: The kwargs for NonCdbAwrAshOverallWaitClass.
        """
        super().__init__(**kwargs)
