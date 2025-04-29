
from app.data.entities.odb.db_top_segment.opt_physical_read import OdbSegmentOptPhysicalRead


class CdbSegmentOptPhysicalRead(OdbSegmentOptPhysicalRead):

    PdbName: str
    
    key_map = {
        'PDB_NAME': 'PdbName',
        **OdbSegmentOptPhysicalRead.key_map
    }

    def __init__(self, **kwargs):
        """
        CdbSegmentOptPhysicalRead model, inheriting from BaseModel.

        Args:
            **kwargs: The kwargs for CdbSegmentOptPhysicalRead.
        """
        super().__init__(**kwargs)
