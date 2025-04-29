
from app.data.entities.odb.db_top_sql.cwait import OdbSqlCwait


class CdbSqlCwait(OdbSqlCwait):

    PdbName: str
    
    key_map = {
        'PDB_NAME': 'PdbName',
        **OdbSqlCwait.key_map
    }

    def __init__(self, **kwargs):
        """
        CdbSqlCwait model, inheriting from BaseModel.

        Args:
            **kwargs: The kwargs for CdbSqlCwait.
        """
        super().__init__(**kwargs)
