from app.data.entities.noncdb.ash.sql_id import NonCdbAshSqlId

class NonCdbAshSqlIdSqContention(NonCdbAshSqlId):

    Sequence: object

    key_map = {
        **NonCdbAshSqlId.key_map,
        'SEQUENCE': 'Sequence'
    }

    def __init__(self, **kwargs):
        """
        NonCdbAshSqlIdSqContention model, inheriting from BaseModel.

        Args:
            **kwargs: The kwargs for NonCdbAshSqlIdSqContention.
        """
        super().__init__(**kwargs)
