from base.domain.base_entity import BaseEntity

class OdbSqlDiskReads(BaseEntity):

    DbName: str
    InstanceName: str
    SqlId: str
    DirectReads: object
    DirectReadsExec: object
    SqlText: str

    key_map = {
        'DB_NAME': 'DbName',
        'INSTANCE_NAME': 'InstanceName',
        'SQL_ID': 'SqlId',
        'DIRECT_READS': 'DirectReads',
        'DIRECT_READS_EXEC': 'DirectReadsExec',
        'SQL_TEXT': 'SqlText'
    }

    def __init__(self, **kwargs):
        """
        OdbSqlDiskReads model, inheriting from BaseModel.

        Args:
            **kwargs: The kwargs for OdbSqlDiskReads.
        """
        super().__init__(**kwargs)
