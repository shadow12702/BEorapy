
from app.data.entities.odb.ash.overall_sql_operation import OdbAshOverallSqlOperation

class CdbAshOverallSqlOperation(OdbAshOverallSqlOperation):
    
    PdbName: str
    

    key_map = {
        'PDB_NAME': 'PdbName',
        **OdbAshOverallSqlOperation.key_map
    }

    def __init__(self, **kwargs):
        """
        CdbAshOverallSqlOperation model, inheriting from BaseModel.

        Args:
            **kwargs: The kwargs for CdbAshOverallSqlOperation.
        """
        super().__init__(**kwargs)
