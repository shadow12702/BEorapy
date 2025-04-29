from app.data.entities.odb.db_top_sql.physical_read_mb import OdbSqlPhysicalReadMb

class CdbSqlPhysicalReadMb(OdbSqlPhysicalReadMb):

    PdbName: str
    
    key_map = {
        'PDB_NAME': 'PdbName',
        **OdbSqlPhysicalReadMb.key_map
    }

    def __init__(self, **kwargs):
        """
        CdbSqlPhysicalReadMb model, inheriting from BaseModel.

        Args:
            **kwargs: The kwargs for CdbSqlPhysicalReadMb.
        """
        super().__init__(**kwargs)
