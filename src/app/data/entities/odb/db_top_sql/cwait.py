from base.domain.base_entity import BaseEntity

class OdbSqlCwait(BaseEntity):

    DbName: str
    InstanceName: str
    SqlId: str
    ClusterWait: object
    ClusterWaitExec: object
    SqlText: str

    key_map = {
        'DB_NAME': 'DbName',
        'INSTANCE_NAME': 'InstanceName',
        'SQL_ID': 'SqlId',
        'CLUSTERWAIT': 'ClusterWait',
        'CLUSTERWAIT_EXEC': 'ClusterWaitExec',
        'SQL_TEXT': 'SqlText'
    }

    def __init__(self, **kwargs):
        """
        OdbSqlCwait model, inheriting from BaseModel.

        Args:
            **kwargs: The kwargs for OdbSqlCwait.
        """
        super().__init__(**kwargs)
