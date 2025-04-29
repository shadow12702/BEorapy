#Description: AppConfigModel
# 

from base.model.mapped_base_model import MappedBaseModel


class AppConfigModel(MappedBaseModel):
    Title: str
    Description: str
    Language : str 
    Version :str
    MaxThread: int