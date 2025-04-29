from base.domain.base_entity import BaseEntity
from numpy import float64

class OdbAshOverallProgram(BaseEntity):

    DbName: str
    InstanceName: str
    Program: str
    Pct: float64

    key_map = {
        'INSTANCE_NAME': 'InstanceName',
        'DB_NAME': 'DbName',
        'PROGRAM': 'Program',
        'PCT': 'Pct'
    }

    def __init__(self, **kwargs):
        """
        OdbAshOverallProgram model, inheriting from BaseModel.

        Args:
            **kwargs: The kwargs for OdbAshOverallProgram.
        """
        super().__init__(**kwargs)
