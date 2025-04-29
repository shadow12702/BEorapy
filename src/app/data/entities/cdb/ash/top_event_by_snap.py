from app.data.entities.odb.ash.top_event_by_snap import OdbAshTopEventBySnap


class CdbAshTopEventBySnap(OdbAshTopEventBySnap):

    PdbName: str
    
    key_map = {
        'PDB_NAME': 'PdbName',
        **OdbAshTopEventBySnap.key_map
    }

    def __init__(self, **kwargs):
        """
        CdbAshTopEventBySnap model, inheriting from BaseModel.

        Args:
            **kwargs: The kwargs for CdbAshTopEventBySnap.
        """
        super().__init__(**kwargs)
