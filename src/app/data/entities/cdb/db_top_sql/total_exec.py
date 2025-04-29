from base.domain.base_entity import BaseEntity
from datetime import datetime

class CdbSqlTotalExec(BaseEntity):

    DbName: str
    InstanceName: str
    PdbName: str
    SqlId: str
    Execs: object
    SqlText: object

    key_map = {
        'DB_NAME': 'DbName',
        'INSTANCE_NAME': 'InstanceName',
        'PDB_NAME': 'PdbName',
        'SQL_ID': 'SqlId',
        'EXECS': 'Execs',
        'SQL_TEXT': 'SqlText'
    }

    def __init__(self, **kwargs):
        """
        CdbSqlTotalExec model, inheriting from BaseModel.

        Args:
            **kwargs: The kwargs for CdbSqlTotalExec.
        """
        super().__init__(**kwargs)
