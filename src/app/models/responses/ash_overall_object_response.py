# 

from typing import List
from pydantic import BaseModel

class ChartModel(BaseModel):
    type: str
    title: str
    x_axis: str
    y_axis: List[str]

class ChartResponse(BaseModel):
    chart_model: ChartModel
    data: list