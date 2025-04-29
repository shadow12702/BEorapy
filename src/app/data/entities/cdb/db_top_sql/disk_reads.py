
from app.data.entities.odb.db_top_sql.disk_reads import OdbSqlDiskReads


class CdbSqlDiskReads(OdbSqlDiskReads):

    PdbName: str
    
    key_map = {
        'PDB_NAME': 'PdbName',
        **OdbSqlDiskReads.key_map
    }

    def __init__(self, **kwargs):
        """
        CdbSqlDiskReads model, inheriting from BaseModel.

        Args:
            **kwargs: The kwargs for CdbSqlDiskReads.
        """
        super().__init__(**kwargs)
