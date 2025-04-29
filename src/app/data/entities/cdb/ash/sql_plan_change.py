from app.data.entities.odb.ash.sql_plan_change import OdbAshSqlPlanChange

class CdbAshSqlPlanChange(OdbAshSqlPlanChange):

    PdbName: str    

    key_map = {
        'PDB_NAME': 'PdbName',
                
    }

    def __init__(self, **kwargs):
        """
        CdbAshSqlPlanChange model, inheriting from BaseModel.

        Args:
            **kwargs: The kwargs for CdbAshSqlPlanChange.
        """
        super().__init__(**kwargs)
