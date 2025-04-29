from base.domain.base_entity import BaseEntity
from numpy import float64

class OdbExtractTopSql(BaseEntity):

    Dbid: float64
    SqlId: str

    key_map = {
        'DBID': 'Dbid',
        'SQL_ID': 'SqlId'
    }

    def __init__(self, **kwargs):
        """
        OdbExtractTopSqlCpu model, inheriting from BaseModel.

        Args:
            **kwargs: The kwargs for OdbExtractTopSqlCpu.
        """
        super().__init__(**kwargs)
