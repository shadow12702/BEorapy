
from app.data.entities.odb.db_top_sql.off_load import OdbSqlOffLoad


class CdbSqlOffLoad(OdbSqlOffLoad):

    PdbName: str
    
    key_map = {
        'PDB_NAME': 'PdbName',
        **OdbSqlOffLoad.key_map
    }

    def __init__(self, **kwargs):
        """
        CdbSqlOffLoad model, inheriting from BaseModel.

        Args:
            **kwargs: The kwargs for CdbSqlOffLoad.
        """
        super().__init__(**kwargs)
