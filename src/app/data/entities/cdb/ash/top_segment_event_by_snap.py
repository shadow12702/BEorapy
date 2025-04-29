
from app.data.entities.cdb.ash.top_segment_by_snap import CdbAshTopSegmentBySnap


class CdbAshTopSegmentEventBySnap(CdbAshTopSegmentBySnap):

    ObjectName: str    

    key_map = {        
        'OBJECT_NAME': 'ObjectName',
        **CdbAshTopSegmentBySnap.key_map
    }

    def __init__(self, **kwargs):
        """
        CdbAshTopSegmentEventBySnap model, inheriting from BaseModel.

        Args:
            **kwargs: The kwargs for CdbAshTopSegmentEventBySnap.
        """
        super().__init__(**kwargs)
