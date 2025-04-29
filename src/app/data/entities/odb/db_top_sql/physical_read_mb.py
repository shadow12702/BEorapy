from base.domain.base_entity import BaseEntity

class OdbSqlPhysicalReadMb(BaseEntity):

    DbName: str
    InstanceName: str
    SqlId: str
    PhysicalReadMb: object
    PhysicalReadMbExec: object
    SqlText: str

    key_map = {
        'DB_NAME': 'DbName',
        'INSTANCE_NAME': 'InstanceName',
        'SQL_ID': 'SqlId',
        'PHYREAD_MB': 'PhysicalReadMb',
        'PHYREAD_MB_EXEC': 'PhysicalReadMbExec',
        'SQL_TEXT': 'SqlText'
    }

    def __init__(self, **kwargs):
        """
        OdbSqlPhysicalReadMb model, inheriting from BaseModel.

        Args:
            **kwargs: The kwargs for OdbSqlPhysicalReadMb.
        """
        super().__init__(**kwargs)
