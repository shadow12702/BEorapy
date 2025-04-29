from base.domain.base_entity import BaseEntity
from numpy import float64

class OdbAshWaitClass(BaseEntity):

    InstanceName: str
    DbName: str
    WaitClass: object
    Percentage: float64

    key_map = {
        'DB_NAME': 'DbName',
        'INSTANCE_NAME': 'InstanceName',
        'WAIT_CLASS': 'WaitClass',
        'PERCENTAGE': 'Percentage'
    }

    def __init__(self, **kwargs):
        """
        OdbAshWaitClass model, inheriting from BaseModel.

        Args:
            **kwargs: The kwargs for OdbAshWaitClass.
        """
        super().__init__(**kwargs)
