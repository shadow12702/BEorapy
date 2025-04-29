from base.domain.base_entity import BaseEntity
from numpy import float64

class OdbAshTopEventBackground(BaseEntity):

    Owner: str
    ObjectName: str
    Partition: object
    Type: str
    Event: str
    Pct: float64

    key_map = {
        'OWNER': 'Owner',
        'OBJECT_NAME': 'ObjectName',
        'PARTITION': 'Partition',
        'TYPE': 'Type',
        'EVENT': 'Event',
        'PCT': 'Pct'
    }

    def __init__(self, **kwargs):
        """
        OdbAshTopEventBackground model, inheriting from BaseModel.

        Args:
            **kwargs: The kwargs for OdbAshTopEventBackground.
        """
        super().__init__(**kwargs)
