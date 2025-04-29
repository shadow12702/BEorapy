
from app.data.entities.odb.ash.top_segment_sql_event_by_snap import OdbAshTopSegmentSqlEventBySnap


class CdbAshTopSegmentSqlEventBySnap(OdbAshTopSegmentSqlEventBySnap):
    
    PdbName: str

    key_map = {
        'PDB_NAME': 'PdbName',
        **OdbAshTopSegmentSqlEventBySnap.key_map
    }

    def __init__(self, **kwargs):
        """
        CdbAshTopSegmentSqlEventBySnap model, inheriting from BaseModel.

        Args:
            **kwargs: The kwargs for CdbAshTopSegmentSqlEventBySnap.
        """
        super().__init__(**kwargs)
