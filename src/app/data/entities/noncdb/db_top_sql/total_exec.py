from base.domain.base_entity import BaseEntity
from datetime import datetime
from numpy import float64

class NonCdbSqlTotalExec(BaseEntity):

    DbName: str
    InstanceName: str
    SqlId: str
    TotalExec: object
    SqlText: str

    key_map = {
        'DB_NAME': 'DbName',
        'INSTANCE_NAME': 'InstanceName',
        'SQL_ID': 'SqlId',
        'TOTALEXEC': 'TotalExec',
        'SQL_TEXT': 'SqlText'
    }

    def __init__(self, **kwargs):
        """
        NonCdbSqlTotalExec model, inheriting from BaseModel.

        Args:
            **kwargs: The kwargs for NonCdbSqlTotalExec.
        """
        super().__init__(**kwargs)
