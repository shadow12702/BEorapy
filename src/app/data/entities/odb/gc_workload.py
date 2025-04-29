from base.domain.base_entity import BaseEntity
from datetime import datetime


class OdbGcWorkload(BaseEntity):

    DbName: str
    InstanceName: str
    SnapTime: datetime
    Gegt:   object
    Gccrrt: object
    Gccrbt: object
    Gccrst: object
    Gccrft: object
    Gccrflp:object
    Gccurt: object
    Gccupt: object
    Gccust: object
    Gccuft: object
    Gccuflp:object

    key_map = {
        'DB_NAME': 'DbName',
        'INSTANCE_NAME': 'InstanceName',
        'SNAP_TIME': 'SnapTime',
        'GEGT': 'Gegt',
        'GCCRRT': 'Gccrrt',
        'GCCRBT': 'Gccrbt',
        'GCCRST': 'Gccrst',
        'GCCRFT': 'Gccrft',
        'GCCRFLP': 'Gccrflp',
        'GCCURT': 'Gccurt',
        'GCCUPT': 'Gccupt',
        'GCCUST': 'Gccust',
        'GCCUFT': 'Gccuft',
        'GCCUFLP': 'Gccuflp'
    }

    def __init__(self, **kwargs):
        """
        OdbGcWorkload model, inheriting from BaseModel.

        Args:
            **kwargs: The kwargs for OdbGcWorkload.
        """
        super().__init__(**kwargs)
