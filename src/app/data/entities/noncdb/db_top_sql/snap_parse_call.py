from base.domain.base_entity import BaseEntity
from datetime import datetime
from numpy import float64

class NonCdbSqlSnapParseCall(BaseEntity):

    DbName: str
    InstanceName: str
    SnapTime: datetime
    SqlId: str
    Parse: object
    Executions: object
    ParseExec: object
    Ratio: float64

    key_map = {
        'DB_NAME': 'DbName',
        'INSTANCE_NAME': 'InstanceName',
        'SNAP_TIME': 'SnapTime',
        'SQL_ID': 'SqlId',
        'PARSE': 'Parse',
        'EXECUTIONS': 'Executions',
        'PARSE_EXEC': 'ParseExec',
        'RATIO': 'Ratio'
    }

    def __init__(self, **kwargs):
        """
        NonCdbSqlSnapParseCall model, inheriting from BaseModel.

        Args:
            **kwargs: The kwargs for NonCdbSqlSnapParseCall.
        """
        super().__init__(**kwargs)
