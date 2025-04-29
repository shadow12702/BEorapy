from base.domain.base_entity import BaseEntity
from numpy import float64

class OdbSegmentChainRow(BaseEntity):

    InstanceName: str
    DbName: str
    Owner: str
    ObjectName: str
    Chainrow: float64

    key_map = {
        'INSTANCE_NAME': 'InstanceName',
        'DB_NAME': 'DbName',
        'OWNER': 'Owner',
        'OBJECT_NAME': 'ObjectName',
        'CHAINROW': 'Chainrow'
    }

    def __init__(self, **kwargs):
        """
        OdbSegmentChainRow model, inheriting from BaseModel.

        Args:
            **kwargs: The kwargs for OdbSegmentChainRow.
        """
        super().__init__(**kwargs)
