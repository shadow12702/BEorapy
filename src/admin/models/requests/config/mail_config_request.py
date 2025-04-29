# Description: MailConfigRequest

from pydantic import BaseModel

class MailSetting(BaseModel):
    sender: str
    password: str
    smtp_server: str
    smtp_port: int
    use_ssl: bool
    
class MailBody(BaseModel):
    activate: str
    lock_account: str
    
class MailConfigRequest(BaseModel):
    config: MailSetting
    body : MailBody
