
from app.data.entities.odb.db_top_segment.physical_read_iops import OdbSegmentPhysicalReadIops


class CdbSegmentPhysicalReadIops(OdbSegmentPhysicalReadIops):

    PdbName: str
    
    key_map = {
        'PDB_NAME': 'PdbName',
        **OdbSegmentPhysicalReadIops.key_map
    }

    def __init__(self, **kwargs):
        """
        CdbSegmentPhysicalReadIops model, inheriting from BaseModel.

        Args:
            **kwargs: The kwargs for CdbSegmentPhysicalReadIops.
        """
        super().__init__(**kwargs)
