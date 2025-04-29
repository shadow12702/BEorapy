from base.domain.base_entity import BaseEntity

class OdbSqlVersions(BaseEntity):

    DbName: str
    InstanceName: str
    SqlId: str
    Version: object
    SqlText: str

    key_map = {
        'DB_NAME': 'DbName',
        'INSTANCE_NAME': 'InstanceName',
        'SQL_ID': 'SqlId',
        'VERSION': 'Version',
        'SQL_TEXT': 'SqlText'
    }

    def __init__(self, **kwargs):
        """
        OdbSqlVersions model, inheriting from BaseModel.

        Args:
            **kwargs: The kwargs for OdbSqlVersions.
        """
        super().__init__(**kwargs)
