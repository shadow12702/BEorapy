from app.data.entities.odb.db_top_segment.block_change import OdbSegmentBlockChange


class CdbSegmentBlockChange(OdbSegmentBlockChange):

    PdbName: str
    
    key_map = {
        'PDB_NAME': 'PdbName',
        **OdbSegmentBlockChange.key_map
    }

    def __init__(self, **kwargs):
        """
        CdbSegmentBlockChange model, inheriting from BaseModel.

        Args:
            **kwargs: The kwargs for CdbSegmentBlockChange.
        """
        super().__init__(**kwargs)
