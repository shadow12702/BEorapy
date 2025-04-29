
from app.data.entities.odb.ash.sql_id import OdbAshSqlId


class CdbAshSqlId(OdbAshSqlId):

    PdbName: str    

    key_map = {
        'PDB_NAME': 'PdbName',
        **OdbAshSqlId.key_map        
    }

    def __init__(self, **kwargs):
        """
        CdbAshSqlId model, inheriting from BaseModel.

        Args:
            **kwargs: The kwargs for CdbAshSqlId.
        """
        super().__init__(**kwargs)
