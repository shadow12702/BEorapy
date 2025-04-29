from app.data.entities.odb.db_top_segment.chain_row import OdbSegmentChainRow


class CdbSegmentChainRow(OdbSegmentChainRow):

    PdbName: str
    
    key_map = {
        'PDB_NAME': 'PdbName',
        **OdbSegmentChainRow.key_map
    }

    def __init__(self, **kwargs):
        """
        CdbSegmentChainRow model, inheriting from BaseModel.

        Args:
            **kwargs: The kwargs for CdbSegmentChainRow.
        """
        super().__init__(**kwargs)
