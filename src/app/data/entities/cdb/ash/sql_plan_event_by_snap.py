

from app.data.entities.odb.ash.sql_plan_event_by_snap import OdbAshSqlPlanEventBySnap


class CdbAshSqlPlanEventBySnap(OdbAshSqlPlanEventBySnap):

    PdbName: str


    key_map = {        
        'PDB_NAME': 'PdbName',
        **OdbAshSqlPlanEventBySnap.key_map
    }

    def __init__(self, **kwargs):
        """
        CdbAshSqlPlanEventBySnap model, inheriting from BaseModel.

        Args:
            **kwargs: The kwargs for CdbAshSqlPlanEventBySnap.
        """
        super().__init__(**kwargs)
