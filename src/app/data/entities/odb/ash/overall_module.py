from base.domain.base_entity import BaseEntity
from numpy import float64

class OdbAshOverallModule(BaseEntity):

    DbName: str
    InstanceName: str
    Module: str
    Pct: float64

    key_map = {
        'INSTANCE_NAME': 'InstanceName',
        'DB_NAME': 'DbName',
        'MODULE': 'Module',
        'PCT': 'Pct'
    }

    def __init__(self, **kwargs):
        """
        OdbAshOverallModule model, inheriting from BaseModel.

        Args:
            **kwargs: The kwargs for OdbAshOverallModule.
        """
        super().__init__(**kwargs)
