from base.domain.base_entity import BaseEntity
from datetime import datetime
from numpy import float64

class CdbMemResize(BaseEntity):

    InstanceName: str
    PdbName: str
    Component: float64
    OperType: str
    Qty: float64

    key_map = {
        'INSTANCE_NAME': 'InstanceName',
        'PDB_NAME': 'PdbName',
        'COMPONENT': 'Component',
        'OPER_TYPE': 'OperType',
        'QTY': 'Qty'
    }

    def __init__(self, **kwargs):
        """
        CdbMemResize model, inheriting from BaseModel.

        Args:
            **kwargs: The kwargs for CdbMemResize.
        """
        super().__init__(**kwargs)
