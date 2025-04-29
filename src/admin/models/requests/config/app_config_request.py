# Description: AppConfigRequest

from pydantic import BaseModel

class AppConfigRequest(BaseModel):
    title: str
    description: str
    language: str
    version: str    
    max_thread: int
