
from app.data.entities.odb.db_top_segment.gc_cr_block_rec import OdbSegmentGcCrBlockRec


class CdbSegmentGcCrBlockRec(OdbSegmentGcCrBlockRec):

    PdbName: str
    
    key_map = {
        'PDB_NAME': 'PdbName',
        **OdbSegmentGcCrBlockRec.key_map
    }

    def __init__(self, **kwargs):
        """
        CdbSegmentGcCrBlockRec model, inheriting from BaseModel.

        Args:
            **kwargs: The kwargs for CdbSegmentGcCrBlockRec.
        """
        super().__init__(**kwargs)
