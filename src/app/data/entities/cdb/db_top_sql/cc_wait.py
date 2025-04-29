from base.domain.base_entity import BaseEntity

class CdbSqlCcWait(BaseEntity):

    DbName: str
    InstanceName: str
    PdbName: str
    SqlId: str
    CcWait: object
    CcWaitExec: object
    SqlText: str

    key_map = {
        'DB_NAME': 'DbName',
        'INSTANCE_NAME': 'InstanceName',
        'PDB_NAME': 'PdbName',
        'SQL_ID': 'SqlId',
        'CCWAIT': 'CcWait',
        'CCWAIT_EXEC': 'CcWaitExec',
        'SQL_TEXT': 'SqlText'
    }

    def __init__(self, **kwargs):
        """
        CdbSqlCcWait model, inheriting from BaseModel.

        Args:
            **kwargs: The kwargs for CdbSqlCcWait.
        """
        super().__init__(**kwargs)
