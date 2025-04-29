
from app.data.entities.odb.ash.overall_wait_class import OdbAshOverallWaitClass


class CdbAshOverallWaitClass(OdbAshOverallWaitClass):

    PdbName: str
    
    key_map = {
        'PDB_NAME': 'PdbName',
        **OdbAshOverallWaitClass.key_map
    }

    def __init__(self, **kwargs):
        """
        CdbAshOverallWaitClass model, inheriting from BaseModel.

        Args:
            **kwargs: The kwargs for CdbAshOverallWaitClass.
        """
        super().__init__(**kwargs)
