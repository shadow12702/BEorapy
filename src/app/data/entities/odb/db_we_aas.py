from base.domain.base_entity import BaseEntity
from datetime import datetime
from numpy import float64

class OdbDbWeAas(BaseEntity):

    SnapId: float64
    SnapTime: datetime
    DbName: str
    InstanceName: str
    EventName: str
    Aas: object
    DbTime: object

    key_map = {
        'SNAP_ID': 'SnapId',
        'SNAP_TIME': 'SnapTime',
        'DB_NAME': 'DbName',
        'INSTANCE_NAME': 'InstanceName',
        'EVENT_NAME': 'EventName',
        'AAS': 'Aas',
        'DB_TIME': 'DbTime'
    }

    def __init__(self, **kwargs):
        """
        DbWeAas model, inheriting from BaseModel.

        Args:
            **kwargs: The kwargs for DbWeAas.
        """
        super().__init__(**kwargs)
