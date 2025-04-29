from base.domain.base_entity import BaseEntity

class OdbSqlElapsed(BaseEntity):

    DbName: str
    InstanceName: str
    SqlId: str
    ElapsedTime: object
    ElapsedTimeExec: object
    SqlText: str

    key_map = {
        'DB_NAME': 'DbName',
        'INSTANCE_NAME': 'InstanceName',
        'SQL_ID': 'SqlId',
        'ELAPSEDTIME': 'ElapsedTime',
        'ELAPSEDTIME_EXEC': 'ElapsedTimeExec',
        'SQL_TEXT': 'SqlText'
    }

    def __init__(self, **kwargs):
        """
        OdbSqlElapsed model, inheriting from BaseModel.

        Args:
            **kwargs: The kwargs for OdbSqlElapsed.
        """
        super().__init__(**kwargs)
