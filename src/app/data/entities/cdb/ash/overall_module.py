
from app.data.entities.odb.ash.overall_module import OdbAshOverallModule


class CdbAshOverallModule(OdbAshOverallModule):

    PdbName: str

    key_map = {
        'PDB_NAME': 'PdbName',
        **OdbAshOverallModule.key_map
    }
    
    def __init__(self, **kwargs):
        """
        CdbAshOverallModule model, inheriting from BaseModel.

        Args:
            **kwargs: The kwargs for CdbAshOverallModule.
        """
        super().__init__(**kwargs)
