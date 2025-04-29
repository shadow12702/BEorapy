from base.domain.base_entity import BaseEntity
from datetime import datetime
from numpy import float64

class NonCdbSqlSnapInvalid(BaseEntity):

    DbName: str
    InstanceName: str
    SnapTime: datetime
    SqlId: str
    Invalid: object
    Executions: object
    InvalidExec: object
    Ratio: float64

    key_map = {
        'DB_NAME': 'DbName',
        'INSTANCE_NAME': 'InstanceName',
        'SNAP_TIME': 'SnapTime',
        'SQL_ID': 'SqlId',
        'INVALID': 'Invalid',
        'EXECUTIONS': 'Executions',
        'INVALID_EXEC': 'InvalidExec',
        'RATIO': 'Ratio'
    }

    def __init__(self, **kwargs):
        """
        NonCdbSqlSnapInvalid model, inheriting from BaseModel.

        Args:
            **kwargs: The kwargs for NonCdbSqlSnapInvalid.
        """
        super().__init__(**kwargs)
