
from app.data.entities.odb.db_top_sql.parse_call import OdbSqlParseCall


class CdbSqlParseCall(OdbSqlParseCall):

    PdbName: str
    
    key_map = {
        'PDB_NAME': 'PdbName',
        **OdbSqlParseCall.key_map
    }

    def __init__(self, **kwargs):
        """
        CdbSqlParseCall model, inheriting from BaseModel.

        Args:
            **kwargs: The kwargs for CdbSqlParseCall.
        """
        super().__init__(**kwargs)
