from base.domain.base_entity import BaseEntity

class OdbSqlOffLoadReturn(BaseEntity):

    DbName: str
    InstanceName: str
    SqlId: str
    OffLoadReturn: object
    OffLoadReturnExec: object
    SqlText: str

    key_map = {
        'DB_NAME': 'DbName',
        'INSTANCE_NAME': 'InstanceName',
        'SQL_ID': 'SqlId',
        'OFFLOADRETURN': 'OffLoadReturn',
        'OFFLOADRETURN_EXEC': 'OffLoadReturnExec',
        'SQL_TEXT': 'SqlText'
    }

    def __init__(self, **kwargs):
        """
        OdbSqlOffLoadReturn model, inheriting from BaseModel.

        Args:
            **kwargs: The kwargs for OdbSqlOffLoadReturn.
        """
        super().__init__(**kwargs)
