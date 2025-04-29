from app.data.entities.odb.ash.event import OdbAshEvent


class CdbAshEvent(OdbAshEvent):
    PdbName: str

    key_map = {
        'PDB_NAME': 'PdbName',
        **OdbAshEvent.key_map
    }
    
    def __init__(self, **kwargs):
        """
        CdbAshEvent model, inheriting from BaseModel.

        Args:
            **kwargs: The kwargs for CdbAshEvent.
        """
        super().__init__(**kwargs)