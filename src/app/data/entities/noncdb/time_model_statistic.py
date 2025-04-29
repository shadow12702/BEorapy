
from numpy import float64
from app.data.entities.odb.time_model_statistic import OdbTimeModelStatistic

class NonCdbTimeModelStatistic(OdbTimeModelStatistic):

    FparseTime   : float64
    ConTime      : float64
    FparsePctDbt : float64
    ConPctDbt    : float64


    key_map = {
        **OdbTimeModelStatistic.key_map,
        'FPARSE_TIME' : 'FparseTime',
        'CON_TIME' : 'ConTime',
        'FPARSE_PCT_DBT' : 'FparsePctDbt',
        'CON_PCT_DBT' : 'ConPctDbt'
    }

    def __init__(self, **kwargs):
        """
        NonCdbTimeModelStatistic model, inheriting from BaseModel.

        Args:
            **kwargs: The kwargs for NonCdbTimeModelStatistic.
        """
        super().__init__(**kwargs)
