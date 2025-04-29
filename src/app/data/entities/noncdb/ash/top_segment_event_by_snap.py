from app.data.entities.odb.ash.top_segment_by_snap import OdbAshTopSegmentBySnap

class NonCdbAshTopSegmentEventBySnap(OdbAshTopSegmentBySnap):
    
    ObjectName: str

    key_map = {
        'OBJECT_NAME': 'ObjectName',
        **OdbAshTopSegmentBySnap.key_map
    }

    def __init__(self, **kwargs):
        """
        NonCdbAshTopSegmentEventBySnap model, inheriting from BaseModel.

        Args:
            **kwargs: The kwargs for NonCdbAshTopSegmentEventBySnap.
        """
        super().__init__(**kwargs)
