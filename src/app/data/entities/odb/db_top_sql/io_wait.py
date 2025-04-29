from base.domain.base_entity import BaseEntity

class OdbSqlIoWait(BaseEntity):

    DbName: str
    InstanceName: str
    SqlId: str
    IoWait: object
    IoWaitExec: object
    SqlText: str

    key_map = {
        'DB_NAME': 'DbName',
        'INSTANCE_NAME': 'InstanceName',
        'SQL_ID': 'SqlId',
        'IOWAIT': 'IoWait',
        'IOWAIT_EXEC': 'IoWaitExec',
        'SQL_TEXT': 'SqlText'
    }

    def __init__(self, **kwargs):
        """
        OdbSqlIoWait model, inheriting from BaseModel.

        Args:
            **kwargs: The kwargs for OdbSqlIoWait.
        """
        super().__init__(**kwargs)
