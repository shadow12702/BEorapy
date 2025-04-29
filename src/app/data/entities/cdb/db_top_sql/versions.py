
from app.data.entities.odb.db_top_sql.versions import OdbSqlVersions


class CdbSqlVersions(OdbSqlVersions):

    PdbName: str
    VersionExec: object
    
    key_map = {
        'PDB_NAME': 'PdbName',
        'VERSION_EXEC': 'VersionExec',
        **OdbSqlVersions.key_map
    }

    def __init__(self, **kwargs):
        """
        CdbSqlVersions model, inheriting from BaseModel.

        Args:
            **kwargs: The kwargs for CdbSqlVersions.
        """
        super().__init__(**kwargs)
