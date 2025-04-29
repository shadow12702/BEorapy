from app.data.entities.odb.dba_history_statistic_global import OdbDbaHistoryStatisticGlobal

class CdbDbaHistoryStatisticGlobal(OdbDbaHistoryStatisticGlobal):

    PdbName: str
    
    key_map = {
        'PDB_NAME': 'PdbName',
        **OdbDbaHistoryStatisticGlobal.key_map
    }

    def __init__(self, **kwargs):
        """
        CdbDbaHistoryStatisticGlobal model, inheriting from BaseModel.

        Args:
            **kwargs: The kwargs for CdbDbaHistoryStatisticGlobal.
        """
        super().__init__(**kwargs)
