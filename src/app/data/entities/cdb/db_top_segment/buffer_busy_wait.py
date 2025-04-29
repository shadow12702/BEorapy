from app.data.entities.odb.db_top_segment.buffer_busy_wait import OdbSegmentBufferBusyWait


class CdbSegmentBufferBusyWait(OdbSegmentBufferBusyWait):

    PdbName: str
    
    key_map = {
        'PDB_NAME': 'PdbName',
        **OdbSegmentBufferBusyWait.key_map
    }

    def __init__(self, **kwargs):
        """
        CdbSegmentBufferBusyWait model, inheriting from BaseModel.

        Args:
            **kwargs: The kwargs for CdbSegmentBufferBusyWait.
        """
        super().__init__(**kwargs)
