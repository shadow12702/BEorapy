from base.domain.base_entity import BaseEntity
from numpy import float64

class NonCdbAwrAshOverallProgram(BaseEntity):

    DbName: str
    InstanceName: str
    Program: float64
    Pct: float64

    key_map = {
        'DB_NAME': 'DbName',
        'INSTANCE_NAME': 'InstanceName',
        'PROGRAM': 'Program',
        'PCT': 'Pct'
    }

    def __init__(self, **kwargs):
        """
        AwrAshOverallProgram model, inheriting from BaseModel.

        Args:
            **kwargs: The kwargs for AwrAshOverallProgram.
        """
        super().__init__(**kwargs)
