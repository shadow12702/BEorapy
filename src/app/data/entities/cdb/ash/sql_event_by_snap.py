from app.data.entities.odb.ash.sql_event_by_snap import OdbAshSqlEventBySnap


class CdbAshSqlEventBySnap(OdbAshSqlEventBySnap):

    PdbName: str

    key_map = {
        'PDB_NAME': 'PdbName',
        **OdbAshSqlEventBySnap.key_map
    }

    def __init__(self, **kwargs):
        """
        CdbAshSqlEventBySnap model, inheriting from BaseModel.

        Args:
            **kwargs: The kwargs for CdbAshSqlEventBySnap.
        """
        super().__init__(**kwargs)
