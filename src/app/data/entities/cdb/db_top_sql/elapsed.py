
from app.data.entities.odb.db_top_sql.elapsed import OdbSqlElapsed


class CdbSqlElapsed(OdbSqlElapsed):

    PdbName: str
    
    key_map = {
        'PDB_NAME': 'PdbName',
        **OdbSqlElapsed.key_map
    }

    def __init__(self, **kwargs):
        """
        CdbSqlElapsed model, inheriting from BaseModel.

        Args:
            **kwargs: The kwargs for CdbSqlElapsed.
        """
        super().__init__(**kwargs)
