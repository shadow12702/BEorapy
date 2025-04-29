from base.domain.base_entity import BaseEntity


class OdbSqlPhysicalWriteIops(BaseEntity):

    DbName: str
    InstanceName: str
    SqlId: str
    PhysicalWriteReqs: object
    PhysicalWriteReqsExec: object
    SqlText: str

    key_map = {
        'DB_NAME': 'DbName',
        'INSTANCE_NAME': 'InstanceName',
        'SQL_ID': 'SqlId',
        'PHYWR_REQS': 'PhysicalWriteReqs',
        'PHYWR_REQS_EXEC': 'PhysicalWriteReqsExec',
        'SQL_TEXT': 'SqlText'
    }

    def __init__(self, **kwargs):
        """
        OdbSqlPhysicalWriteIops model, inheriting from BaseModel.

        Args:
            **kwargs: The kwargs for OdbSqlPhysicalWriteIops.
        """
        super().__init__(**kwargs)
