
from app.data.entities.odb.ash.overall_program import OdbAshOverallProgram

class CdbAshOverallProgram(OdbAshOverallProgram):

    PdbName: str

    key_map = {        
        'PDB_NAME': 'PdbName',
        **OdbAshOverallProgram.key_map
    }

    def __init__(self, **kwargs):
        """
        CdbAshOverallProgram model, inheriting from BaseModel.

        Args:
            **kwargs: The kwargs for CdbAshOverallProgram.
        """
        super().__init__(**kwargs)
