from base.domain.base_entity import BaseEntity
from datetime import datetime
from numpy import float64

class OdbBufferPoolConfig(BaseEntity):

    DbName: str
    InstanceName: str
    SnapId: float64
    SnapTime: datetime
    Name: str
    Numbufs: float64
    Poolhr: float64
    Buffs: float64
    Conget: float64
    Phread: float64
    Phwrite: float64
    Fbwait: float64
    Wcwait: float64
    Bbwait: float64
    Sumscan: float64
    Sumwrite: float64

    key_map = {
        'DB_NAME': 'DbName',
        'INSTANCE_NAME': 'InstanceName',
        'SNAP_ID': 'SnapId',
        'SNAP_TIME': 'SnapTime',
        'NAME': 'Name',
        'NUMBUFS': 'Numbufs',
        'POOLHR': 'Poolhr',
        'BUFFS': 'Buffs',
        'CONGET': 'Conget',
        'PHREAD': 'Phread',
        'PHWRITE': 'Phwrite',
        'FBWAIT': 'Fbwait',
        'WCWAIT': 'Wcwait',
        'BBWAIT': 'Bbwait',
        'SUMSCAN': 'Sumscan',
        'SUMWRITE': 'Sumwrite'
    }

    def __init__(self, **kwargs):
        """
        OdbBufferPoolConfig model, inheriting from BaseModel.

        Args:
            **kwargs: The kwargs for OdbBufferPoolConfig.
        """
        super().__init__(**kwargs)
