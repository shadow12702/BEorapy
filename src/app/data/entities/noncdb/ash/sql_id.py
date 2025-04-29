
from app.data.entities.odb.ash.sql_id import OdbAshSqlId


class NonCdbAshSqlId(OdbAshSqlId):

    DbName: str    

    key_map = {
        'DB_NAME': 'DbName',
        **OdbAshSqlId.key_map        
    }

    def __init__(self, **kwargs):
        """
        NonCdbAshSqlId model, inheriting from BaseModel.

        Args:
            **kwargs: The kwargs for NonCdbAshSqlId.
        """
        super().__init__(**kwargs)
