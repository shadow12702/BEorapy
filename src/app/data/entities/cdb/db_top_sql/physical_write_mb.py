from app.data.entities.odb.db_top_sql.physical_write_mb import OdbSqlPhysicalWriteMb

class CdbSqlPhysicalWriteMb(OdbSqlPhysicalWriteMb):

    PdbName: str
    
    key_map = {
        'PDB_NAME': 'PdbName',
        **OdbSqlPhysicalWriteMb.key_map
    }

    def __init__(self, **kwargs):
        """
        CdbSqlPhysicalWriteMb model, inheriting from BaseModel.

        Args:
            **kwargs: The kwargs for CdbSqlPhysicalWriteMb.
        """
        super().__init__(**kwargs)
