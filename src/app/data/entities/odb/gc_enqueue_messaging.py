from base.domain.base_entity import BaseEntity
from datetime import datetime
from numpy import float64

class OdbGcEnqueueMessaging(BaseEntity):

    DbName: str
    InstanceName: str
    SnapId: float64
    SnapTime: datetime
    Msgsqt: object
    Msgsqtk: object
    Msgrqt: object
    Pmpt: object
    Npmpt: object
    Dmsdp: object
    Dmsip: object
    Dmfcp: object


    key_map = {
        'DB_NAME' : 'DbName',
        'INSTANCE_NAME' : 'InstanceName',
        'SNAP_ID' : 'SnapId',
        'SNAP_TIME' : 'SnapTime',
        'MSGSQT' : 'Msgsqt',
        'MSGSQTK' : 'Msgsqtk',
        'MSGRQT' : 'Msgrqt',
        'PMPT' : 'Pmpt',
        'NPMPT' : 'Npmpt',
        'DMSDP' : 'Dmsdp',
        'DMSIP' : 'Dmsip',
        'DMFCP' : 'Dmfcp'
    }

    def __init__(self, **kwargs):
        """
        OdbGcEnqueueMessaging model, inheriting from BaseModel.

        Args:
            **kwargs: The kwargs for OdbGcEnqueueMessaging.
        """
        super().__init__(**kwargs)
