from app.data.entities.odb.db_top_segment.logical_read import OdbSegmentLogicalRead

class CdbSegmentLogicalRead(OdbSegmentLogicalRead):

    PdbName: str
    
    key_map = {
        'PDB_NAME': 'PdbName',
        **OdbSegmentLogicalRead.key_map
    }

    def __init__(self, **kwargs):
        """
        CdbSegmentLogicalRead model, inheriting from BaseModel.

        Args:
            **kwargs: The kwargs for CdbSegmentLogicalRead.
        """
        super().__init__(**kwargs)
