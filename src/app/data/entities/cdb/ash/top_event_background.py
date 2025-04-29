from app.data.entities.odb.ash.top_event_background import OdbAshTopEventBackground

class CdbAshTopEventBackground(OdbAshTopEventBackground):

    PdbName: str
    
    key_map = {
        'PDB_NAME': 'PdbName',
        **OdbAshTopEventBackground.key_map
    }

    def __init__(self, **kwargs):
        """
        CdbAshTopEventBackground model, inheriting from BaseModel.

        Args:
            **kwargs: The kwargs for CdbAshTopEventBackground.
        """
        super().__init__(**kwargs)
