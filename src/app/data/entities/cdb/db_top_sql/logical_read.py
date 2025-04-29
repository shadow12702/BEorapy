

from app.data.entities.odb.db_top_sql.logical_read import OdbSqlLogicalRead


class CdbSqlLogicalRead(OdbSqlLogicalRead):

    PdbName: str
    
    key_map = {
        'PDB_NAME': 'PdbName',
        **OdbSqlLogicalRead.key_map
    }

    def __init__(self, **kwargs):
        """
        CdbSqlLogicalRead model, inheriting from BaseModel.

        Args:
            **kwargs: The kwargs for CdbSqlLogicalRead.
        """
        super().__init__(**kwargs)
