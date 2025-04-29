
from app.data.entities.odb.db_top_segment.row_lock import OdbSegmentRowLock


class CdbSegmentRowLock(OdbSegmentRowLock):

    PdbName: str
    
    key_map = {
        'PDB_NAME': 'PdbName',
        **OdbSegmentRowLock.key_map
    }

    def __init__(self, **kwargs):
        """
        CdbSegmentRowLock model, inheriting from BaseModel.

        Args:
            **kwargs: The kwargs for CdbSegmentRowLock.
        """
        super().__init__(**kwargs)
