
from app.data.entities.odb.db_top_sql.physical_read_iops import OdbSqlPhysicalReadIops


class CdbSqlPhysicalReadIops(OdbSqlPhysicalReadIops):

    PdbName: str
    
    key_map = {
        'PDB_NAME': 'PdbName',
        **OdbSqlPhysicalReadIops.key_map
    }

    def __init__(self, **kwargs):
        """
        CdbSqlPhysicalReadIops model, inheriting from BaseModel.

        Args:
            **kwargs: The kwargs for CdbSqlPhysicalReadIops.
        """
        super().__init__(**kwargs)
