from base.domain.base_entity import BaseEntity
from numpy import float64

class OdbAshEvent(BaseEntity):
    
    Owner: str
    ObjectName: str
    Partition: float64
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
        OdbAshEvent model, inheriting from BaseModel.

        Args:
            **kwargs: The kwargs for OdbAshEvent.
        """
        super().__init__(**kwargs)

