
from app.data.entities.odb.db_top_segment.physical_write import OdbSegmentPhysicalWrite


class CdbSegmentPhysicalWrite(OdbSegmentPhysicalWrite):

    PdbName: str
    
    key_map = {
        'PDB_NAME': 'PdbName',
        **OdbSegmentPhysicalWrite.key_map
    }

    def __init__(self, **kwargs):
        """
        CdbSegmentPhysicalWrite model, inheriting from BaseModel.

        Args:
            **kwargs: The kwargs for CdbSegmentPhysicalWrite.
        """
        super().__init__(**kwargs)
