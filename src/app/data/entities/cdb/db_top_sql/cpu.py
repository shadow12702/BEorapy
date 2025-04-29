from app.data.entities.odb.db_top_sql.cpu import OdbSqlCpu


class CdbSqlCpu(OdbSqlCpu):

    PdbName: str
    
    key_map = {
        'PDB_NAME': 'PdbName',
        **OdbSqlCpu.key_map
    }

    def __init__(self, **kwargs):
        """
        CdbSqlCpu model, inheriting from BaseModel.

        Args:
            **kwargs: The kwargs for CdbSqlCpu.
        """
        super().__init__(**kwargs)
