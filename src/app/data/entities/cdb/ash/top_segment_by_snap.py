
from app.data.entities.odb.ash.top_segment_by_snap import OdbAshTopSegmentBySnap


class CdbAshTopSegmentBySnap(OdbAshTopSegmentBySnap):

    PdbName: str
    
    key_map = {        
        'PDB_NAME': 'PdbName',
        **OdbAshTopSegmentBySnap.key_map
    }

    def __init__(self, **kwargs):
        """
        CdbAshTopSegmentBySnap model, inheriting from BaseModel.

        Args:
            **kwargs: The kwargs for CdbAshTopSegmentBySnap.
        """
        super().__init__(**kwargs)
