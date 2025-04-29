
from app.data.entities.odb.db_top_segment.itl_waits import OdbSegmentItlWaits


class CdbSegmentItlWaits(OdbSegmentItlWaits):

    PdbName: str
    
    key_map = {
        'PDB_NAME': 'PdbName',
        **OdbSegmentItlWaits.key_map
    }

    def __init__(self, **kwargs):
        """
        CdbSegmentItlWaits model, inheriting from BaseModel.

        Args:
            **kwargs: The kwargs for CdbSegmentItlWaits.
        """
        super().__init__(**kwargs)
