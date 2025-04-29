from app.data.entities.odb.db_top_segment.physical_write_iops import OdbSegmentPhysicalWriteIops


class CdbSegmentPhysicalWriteIops(OdbSegmentPhysicalWriteIops):

    PdbName: str
    
    key_map = {
        'PDB_NAME': 'PdbName',
        **OdbSegmentPhysicalWriteIops.key_map
    }

    def __init__(self, **kwargs):
        """
        CdbSegmentPhysicalWriteIops model, inheriting from BaseModel.

        Args:
            **kwargs: The kwargs for CdbSegmentPhysicalWriteIops.
        """
        super().__init__(**kwargs)
