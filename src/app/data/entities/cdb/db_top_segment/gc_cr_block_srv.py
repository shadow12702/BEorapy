
from app.data.entities.odb.db_top_segment.gc_cr_block_srv import OdbSegmentGcCrBlockSrv


class CdbSegmentGcCrBlockSrv(OdbSegmentGcCrBlockSrv):

    PdbName: str
    
    key_map = {
        'PDB_NAME': 'PdbName',
        **OdbSegmentGcCrBlockSrv.key_map
    }

    def __init__(self, **kwargs):
        """
        CdbSegmentGcCrBlockSrv model, inheriting from BaseModel.

        Args:
            **kwargs: The kwargs for CdbSegmentGcCrBlockSrv.
        """
        super().__init__(**kwargs)
