from base.domain.base_entity import BaseEntity
from datetime import datetime
from numpy import float64

class NonCdbMemResize(BaseEntity):

    DbName: str
    InstanceName: str
    Component: float64
    OperType: str
    Qty: float64

    key_map = {
        'DB_NAME': 'DbName',
        'INSTANCE_NAME': 'InstanceName',
        'COMPONENT': 'Component',
        'OPER_TYPE': 'OperType',
        'QTY': 'Qty'
    }

    def __init__(self, **kwargs):
        """
        NonCdbMemResize model, inheriting from BaseModel.

        Args:
            **kwargs: The kwargs for NonCdbMemResize.
        """
        super().__init__(**kwargs)
