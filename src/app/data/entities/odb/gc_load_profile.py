from base.domain.base_entity import BaseEntity
from datetime import datetime

class OdbGcLoadProfile(BaseEntity):

    DbName: str
    InstanceName: str
    SnapTime: datetime
    CrBlksRecv: object
    CrBlksServ: object
    CurBlksRecv:object
    CurBlksServ:object
    GcsMsgRecv: object
    GcsMsgSent: object
    GesMsgRecv: object
    GesMsgSent: object
    Icn: object

    key_map = {
        'DB_NAME': 'DbName',
        'INSTANCE_NAME': 'InstanceName',
        'SNAP_TIME': 'SnapTime',
        'CR_BLKS_RECV': 'CrBlksRecv',
        'CR_BLKS_SERV': 'CrBlksServ',
        'CUR_BLKS_RECV': 'CurBlksRecv',
        'CUR_BLKS_SERV': 'CurBlksServ',
        'GCS_MSG_RECV': 'GcsMsgRecv',
        'GCS_MSG_SENT': 'GcsMsgSent',
        'GES_MSG_RECV': 'GesMsgRecv',
        'GES_MSG_SENT': 'GesMsgSent',
        'ICN': 'Icn'
    }

    def __init__(self, **kwargs):
        """
        OdbGcLoadProfile model, inheriting from BaseModel.

        Args:
            **kwargs: The kwargs for OdbGcLoadProfile.
        """
        super().__init__(**kwargs)
