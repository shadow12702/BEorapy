from base.domain.base_entity import BaseEntity

class OdbSqlPhysicalReadIops(BaseEntity):

    DbName: str
    InstanceName: str
    SqlId: str
    PhysicalReadReqs: object
    PhysicalReadReqsExec: object
    SqlText: str

    key_map = {
        'DB_NAME': 'DbName',
        'INSTANCE_NAME': 'InstanceName',
        'SQL_ID': 'SqlId',
        'PHYRD_REQS': 'PhysicalReadReqs',
        'PHYRD_REQS_EXEC': 'PhysicalReadReqsExec',
        'SQL_TEXT': 'SqlText'
    }

    def __init__(self, **kwargs):
        """
        OdbSqlPhysicalReadIops model, inheriting from BaseModel.

        Args:
            **kwargs: The kwargs for OdbSqlPhysicalReadIops.
        """
        super().__init__(**kwargs)
