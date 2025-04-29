
from app.data.entities.odb.db_top_segment.physical_write_dir import OdbSegmentPhysicalWriteDir


class CdbSegmentPhysicalWriteDir(OdbSegmentPhysicalWriteDir):

    PdbName: str
    
    key_map = {
        'PDB_NAME': 'PdbName',
        **OdbSegmentPhysicalWriteDir.key_map
    }

    def __init__(self, **kwargs):
        """
        CdbSegmentPhysicalWriteDir model, inheriting from BaseModel.

        Args:
            **kwargs: The kwargs for CdbSegmentPhysicalWriteDir.
        """
        super().__init__(**kwargs)
