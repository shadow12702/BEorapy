
from app.data.entities.odb.db_top_sql.io_wait import OdbSqlIoWait


class CdbSqlIoWait(OdbSqlIoWait):

    PdbName: str
    
    key_map = {
        'PDB_NAME': 'PdbName',
        **OdbSqlIoWait.key_map
    }

    def __init__(self, **kwargs):
        """
        CdbSqlIoWait model, inheriting from BaseModel.

        Args:
            **kwargs: The kwargs for CdbSqlIoWait.
        """
        super().__init__(**kwargs)
