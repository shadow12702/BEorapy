from app.data.entities.odb.db_top_sql.physical_write_iops import OdbSqlPhysicalWriteIops

class CdbSqlPhysicalWriteIops(OdbSqlPhysicalWriteIops):

    PdbName: str
    
    key_map = {
        'PDB_NAME': 'PdbName',
        **OdbSqlPhysicalWriteIops.key_map
    }

    def __init__(self, **kwargs):
        """
        CdbSqlPhysicalWriteIops model, inheriting from BaseModel.

        Args:
            **kwargs: The kwargs for CdbSqlPhysicalWriteIops.
        """
        super().__init__(**kwargs)
