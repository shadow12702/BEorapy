from base.domain.base_entity import BaseEntity
from numpy import float64

class OdbAshOverallWaitClass(BaseEntity):

    InstanceName: str
    DbName: str
    WaitClass: object
    Pct: float64

    key_map = {
        'INSTANCE_NAME': 'InstanceName',
        'DB_NAME': 'DbName',
        'WAIT_CLASS': 'WaitClass',
        'PCT': 'Pct'
    }

    def __init__(self, **kwargs):
        """
        OdbAshOverallWaitClass model, inheriting from BaseModel.

        Args:
            **kwargs: The kwargs for OdbAshOverallWaitClass.
        """
        super().__init__(**kwargs)
