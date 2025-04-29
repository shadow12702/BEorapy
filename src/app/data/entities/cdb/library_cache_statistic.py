from app.data.entities.odb.library_cache_statistic import OdbLibraryCacheStatistic

class CdbLibraryCacheStatistic(OdbLibraryCacheStatistic):

    PdbName: str
    
    key_map = {
        'PDB_NAME': 'PdbName',
        **OdbLibraryCacheStatistic.key_map
    }

    def __init__(self, **kwargs):
        """
        CdbLibraryCacheStatistic model, inheriting from BaseModel.

        Args:
            **kwargs: The kwargs for CdbLibraryCacheStatistic.
        """
        super().__init__(**kwargs)
