from base.domain.base_entity import BaseEntity

class OdbSqlPhysicalWriteMb(BaseEntity):

    DbName: str
    InstanceName: str
    SqlId: str
    PhysicalWriteMb: object
    PhysicalWriteMbExec: object
    SqlText: str

    key_map = {
        'DB_NAME': 'DbName',
        'INSTANCE_NAME': 'InstanceName',
        'SQL_ID': 'SqlId',
        'PHYWRITE_MB': 'PhysicalWriteMb',
        'PHYWRITE_MB_EXEC': 'PhysicalWriteMbExec',
        'SQL_TEXT': 'SqlText'
    }

    def __init__(self, **kwargs):
        """
        OdbSqlPhysicalWriteMb model, inheriting from BaseModel.

        Args:
            **kwargs: The kwargs for OdbSqlPhysicalWriteMb.
        """
        super().__init__(**kwargs)
