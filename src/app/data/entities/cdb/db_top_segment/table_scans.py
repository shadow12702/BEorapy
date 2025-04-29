
from app.data.entities.odb.db_top_segment.table_scans import OdbSegmentTableScans


class CdbSegmentTableScans(OdbSegmentTableScans):

    PdbName: str

    key_map = {
        'PDB_NAME': 'PdbName',
        **OdbSegmentTableScans.key_map
    }

    def __init__(self, **kwargs):
        """
        CdbSegmentTableScans model, inheriting from BaseModel.

        Args:
            **kwargs: The kwargs for CdbSegmentTableScans.
        """
        super().__init__(**kwargs)
