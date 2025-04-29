
from app.data.entities.odb.db_top_segment.gc_current_block_srv import OdbSegmentGcCurrentBlockSrv


class CdbSegmentGcCurrentBlockSrv(OdbSegmentGcCurrentBlockSrv):

    PdbName: str
    
    key_map = {
        'PDB_NAME': 'PdbName',
        **OdbSegmentGcCurrentBlockSrv.key_map
    }

    def __init__(self, **kwargs):
        """
        CdbSegmentGcCurrentBlockSrv model, inheriting from BaseModel.

        Args:
            **kwargs: The kwargs for CdbSegmentGcCurrentBlockSrv.
        """
        super().__init__(**kwargs)
