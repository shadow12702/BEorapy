from base.domain.base_entity import BaseEntity

class OdbSqlOffLoad(BaseEntity):

    DbName: str
    InstanceName: str
    SqlId: str
    OffLoad: object
    OffLoadExec: object
    SqlText: str

    key_map = {
        'DB_NAME': 'DbName',
        'INSTANCE_NAME': 'InstanceName',
        'SQL_ID': 'SqlId',
        'OFFLOAD': 'OffLoad',
        'OFFLOAD_EXEC': 'OffLoadExec',
        'SQL_TEXT': 'SqlText'
    }

    def __init__(self, **kwargs):
        """
        OdbSqlOffLoad model, inheriting from BaseModel.

        Args:
            **kwargs: The kwargs for OdbSqlOffLoad.
        """
        super().__init__(**kwargs)
