from base.domain.base_entity import BaseEntity

class OdbSqlCpu(BaseEntity):

    DbName: str
    InstanceName: str
    SqlId: str
    CpuTime: object
    CpuTimeExec: object
    SqlText: str

    key_map = {
        'DB_NAME': 'DbName',
        'INSTANCE_NAME': 'InstanceName',
        'SQL_ID': 'SqlId',
        'CPUTIME': 'CpuTime',
        'CPUTIME_EXEC': 'CpuTimeExec',
        'SQL_TEXT': 'SqlText'
    }

    def __init__(self, **kwargs):
        """
        OdbSqlCpu model, inheriting from BaseModel.

        Args:
            **kwargs: The kwargs for OdbSqlCpu.
        """
        super().__init__(**kwargs)
