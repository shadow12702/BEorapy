from base.domain.base_entity import BaseEntity

class OdbSqlLogicalRead(BaseEntity):

    DbName: str
    InstanceName: str
    SqlId: str
    LogicalReads: object
    LogicalReadsExec: object
    SqlText: str

    key_map = {
        'DB_NAME': 'DbName',
        'INSTANCE_NAME': 'InstanceName',
        'SQL_ID': 'SqlId',
        'LOGICAL_READS': 'LogicalReads',
        'LOGICAL_READS_EXEC': 'LogicalReadsExec',
        'SQL_TEXT': 'SqlText'
    }

    def __init__(self, **kwargs):
        """
        OdbSqlLogicalRead model, inheriting from BaseModel.

        Args:
            **kwargs: The kwargs for OdbSqlLogicalRead.
        """
        super().__init__(**kwargs)
