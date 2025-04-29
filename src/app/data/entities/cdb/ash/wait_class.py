from app.data.entities.odb.ash.wait_class import OdbAshWaitClass

class CdbAshWaitClass(OdbAshWaitClass):

    PdbName: str
    
    key_map = {
        'PDB_NAME': 'PdbName',
        **OdbAshWaitClass.key_map
    }

    def __init__(self, **kwargs):
        """
        CdbAshWaitClass model, inheriting from BaseModel.

        Args:
            **kwargs: The kwargs for CdbAshWaitClass.
        """
        super().__init__(**kwargs)
