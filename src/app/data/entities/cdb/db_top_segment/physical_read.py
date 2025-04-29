
from app.data.entities.odb.db_top_segment.physical_read import OdbSegmentPhysicalRead


class CdbSegmentPhysicalRead(OdbSegmentPhysicalRead):

    PdbName: str
    
    key_map = {
        'PDB_NAME': 'PdbName',
        **OdbSegmentPhysicalRead.key_map
    }

    def __init__(self, **kwargs):
        """
        CdbSegmentPhysicalRead model, inheriting from BaseModel.

        Args:
            **kwargs: The kwargs for CdbSegmentPhysicalRead.
        """
        super().__init__(**kwargs)
