

from app.data.entities.odb.db_top_segment.physical_read_dir import OdbSegmentPhysicalReadDir


class CdbSegmentPhysicalReadDir(OdbSegmentPhysicalReadDir):

    PdbName: str
    
    key_map = {
        'PDB_NAME': 'PdbName',
        **OdbSegmentPhysicalReadDir.key_map
    }

    def __init__(self, **kwargs):
        """
        CdbSegmentPhysicalReadDir model, inheriting from BaseModel.

        Args:
            **kwargs: The kwargs for CdbSegmentPhysicalReadDir.
        """
        super().__init__(**kwargs)
