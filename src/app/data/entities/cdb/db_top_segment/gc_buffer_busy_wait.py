
from app.data.entities.odb.db_top_segment.gc_buffer_busy_wait import OdbSegmentGcBufferBusyWait


class CdbSegmentGcBufferBusyWait(OdbSegmentGcBufferBusyWait):

    PdbName: str
    
    key_map = {
        'PDB_NAME': 'PdbName',
        **OdbSegmentGcBufferBusyWait.key_map
    }

    def __init__(self, **kwargs):
        """
        CdbSegmentGcBufferBusyWait model, inheriting from BaseModel.

        Args:
            **kwargs: The kwargs for CdbSegmentGcBufferBusyWait.
        """
        super().__init__(**kwargs)
