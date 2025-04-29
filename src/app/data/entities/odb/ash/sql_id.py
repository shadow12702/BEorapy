from base.domain.base_entity import BaseEntity
from numpy import float64

class OdbAshSqlId(BaseEntity):
    
    SqlId: str
    Event: str
    Pct: float64

    key_map = {        
        'SQL_ID': 'SqlId',
        'EVENT': 'Event',
        'PCT': 'Pct'
    }

    def __init__(self, **kwargs):
        """
        OdbAshSqlId model, inheriting from BaseModel.

        Args:
            **kwargs: The kwargs for OdbAshSqlId.
        """
        super().__init__(**kwargs)
