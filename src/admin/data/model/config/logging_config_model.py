#Description: LoggingConfigModel
# 
from base.model.mapped_base_model import MappedBaseModel

class LoggingConfigModel(MappedBaseModel):
    Level: str
    Directory: str
    DateFormat: str
    LogFormat: str
    FileSuffix: str