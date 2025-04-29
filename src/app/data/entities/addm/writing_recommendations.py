from base.domain.base_entity import BaseEntity
from datetime import datetime
from numpy import  int64

class WritingRecommendations(BaseEntity):    

    BeginTime: datetime
    TaskName: str
    Rank: int64
    Type: str
    Command: str
    ActionMessage: str

    key_map = {
        'BEGINTIME': 'BeginTime',
        'TASK_NAME': 'TaskName',
        'RANK': 'Rank',
        'TYPE': 'Type',
        'COMMAND': 'Command',
        'ACTION_MESSAGE': 'ActionMessage'
    }

    def __init__(self, **kwargs):
        """WritingRecommendations model, inheriting from BaseModel.

        :param **kwargs: The kwargs for WritingRecommendations.
        """
        super().__init__(**kwargs)
