from base.domain.base_entity import BaseEntity
from numpy import float64

class OdbDbInfo(BaseEntity):

    StatName: str
    StatValue: float64

    key_map = {
        'STAT_NAME': 'StatName',
        'STAT_VALUE': 'StatValue'
    }

    def __init__(self, **kwargs):
        """
        OdbDbInfo model, inheriting from BaseModel.

        Args:
            **kwargs: The kwargs for OdbDbInfo.
        """
        super().__init__(**kwargs)
