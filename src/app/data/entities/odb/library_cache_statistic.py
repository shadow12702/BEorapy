from base.domain.base_entity import BaseEntity
from datetime import datetime

class OdbLibraryCacheStatistic(BaseEntity):

    DbName: str
    InstanceName: str
    SnapTime: datetime
    Namespace: str
    Reloads: object
    Invalid: object

    key_map = {
        'DB_NAME': 'DbName',
        'INSTANCE_NAME': 'InstanceName',
        'SNAP_TIME': 'SnapTime',
        'NAMESPACE': 'Namespace',
        'RELOADS': 'Reloads',
        'INVALID': 'Invalid'
    }

    def __init__(self, **kwargs):
        """
        OdbLibraryCacheStatistic model, inheriting from BaseModel.

        Args:
            **kwargs: The kwargs for OdbLibraryCacheStatistic.
        """
        super().__init__(**kwargs)
