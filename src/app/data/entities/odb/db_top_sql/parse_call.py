from base.domain.base_entity import BaseEntity

class OdbSqlParseCall(BaseEntity):

    DbName: str
    InstanceName: str
    SqlId: str
    ParseCall: object
    ParseCallExec: object
    SqlText: str

    key_map = {
        'DB_NAME': 'DbName',
        'INSTANCE_NAME': 'InstanceName',
        'SQL_ID': 'SqlId',
        'PARSECALL': 'ParseCall',
        'PARSECALL_EXEC': 'ParseCallExec',
        'SQL_TEXT': 'SqlText'
    }

    def __init__(self, **kwargs):
        """
        OdbSqlParseCall model, inheriting from BaseModel.

        Args:
            **kwargs: The kwargs for OdbSqlParseCall.
        """
        super().__init__(**kwargs)
