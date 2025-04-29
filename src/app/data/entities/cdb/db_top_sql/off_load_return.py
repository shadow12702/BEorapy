
from app.data.entities.odb.db_top_sql.off_load_return import OdbSqlOffLoadReturn

class CdbSqlOffLoadReturn(OdbSqlOffLoadReturn):

    PdbName: str
    
    key_map = {
        'PDB_NAME': 'PdbName',
        **OdbSqlOffLoadReturn.key_map
    }

    def __init__(self, **kwargs):
        """
        CdbSqlOffLoadReturn model, inheriting from BaseModel.

        Args:
            **kwargs: The kwargs for CdbSqlOffLoadReturn.
        """
        super().__init__(**kwargs)
