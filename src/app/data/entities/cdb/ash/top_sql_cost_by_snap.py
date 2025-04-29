
from app.data.entities.odb.ash.top_sql_cost_by_snap import OdbAshTopSqlCostBySnap


class CdbAshTopSqlCostBySnap(OdbAshTopSqlCostBySnap):

    PdbName: str

    key_map = {
        'PDB_NAME' : 'PdbName',
        **OdbAshTopSqlCostBySnap.key_map
    }

    def __init__(self, **kwargs):
        """
        CdbAshTopSqlCostBySnap model, inheriting from BaseModel.

        Args:
            **kwargs: The kwargs for CdbAshTopSqlCostBySnap.
        """
        super().__init__(**kwargs)
