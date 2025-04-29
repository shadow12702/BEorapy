from base.domain.base_entity import BaseEntity
from numpy import float64

class OdbSegmentTableScans(BaseEntity):

    DbName: str
    InstanceName: str
    Owner: str
    ObjectName: str
    Tablescans: float64

    key_map = {
        'DB_NAME': 'DbName',
        'INSTANCE_NAME': 'InstanceName',
        'OWNER': 'Owner',
        'OBJECT_NAME': 'ObjectName',
        'TABLESCANS': 'Tablescans'
    }

    def __init__(self, **kwargs):
        """
        OdbSegmentTableScans model, inheriting from BaseModel.

        Args:
            **kwargs: The kwargs for OdbSegmentTableScans.
        """
        super().__init__(**kwargs)
