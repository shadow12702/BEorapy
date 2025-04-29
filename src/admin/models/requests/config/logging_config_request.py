# Description: LoggingConfigRequest

from pydantic import BaseModel

class LoggingConfigRequest(BaseModel):
    directory: str
    level: str
    filename_suffix: str
