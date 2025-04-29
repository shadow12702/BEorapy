#Description: MailConfigModel
# 
from pydantic import BaseModel 

class MailConfig(BaseModel):
    Sender:str
    Password: str
    SmtpServer : str
    SmtpPort: int
    UseSsl: bool    
    
class MailBody(BaseModel):
    Activate: str
    LockAccount: str

class MailConfigModel(BaseModel):    
    config: MailConfig
    body: MailBody
    