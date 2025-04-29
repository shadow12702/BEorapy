
from app.data.entities.cdb.ash.sql_id import CdbAshSqlId


class CdbAshSqlIdSqContention(CdbAshSqlId):
    
    Sequence: object

    key_map = {        
        **CdbAshSqlId.key_map,
        'SEQUENCE': 'Sequence'        
    }

    def __init__(self, **kwargs):
        """
        CdbAshSqlIdSqContention model, inheriting from BaseModel.

        Args:
            **kwargs: The kwargs for CdbAshSqlIdSqContention.
        """
        super().__init__(**kwargs)
