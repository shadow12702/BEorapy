from app.data.entities.odb.latch_statistic import OdbLatchStatistic

class CdbLatchStatistic(OdbLatchStatistic):

    PdbName: str
    
    key_map = {
        'PDB_NAME': 'PdbName',
        **OdbLatchStatistic.key_map
    }

    def __init__(self, **kwargs):
        """
        CdbLatchStatistic model, inheriting from BaseModel.

        Args:
            **kwargs: The kwargs for CdbLatchStatistic.
        """
        super().__init__(**kwargs)
