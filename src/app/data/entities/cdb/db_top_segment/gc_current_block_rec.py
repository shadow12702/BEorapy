
from app.data.entities.odb.db_top_segment.gc_current_block_rec import OdbSegmentGcCurrentBlockRec


class CdbSegmentGcCurrentBlockRec(OdbSegmentGcCurrentBlockRec):

    PdbName: str
    
    key_map = {
        'PDB_NAME': 'PdbName',
        **OdbSegmentGcCurrentBlockRec.key_map
    }

    def __init__(self, **kwargs):
        """
        CdbSegmentGcCurrentBlockRec model, inheriting from BaseModel.

        Args:
            **kwargs: The kwargs for CdbSegmentGcCurrentBlockRec.
        """
        super().__init__(**kwargs)
