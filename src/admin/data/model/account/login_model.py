# Description: LoginModel

from datetime import datetime
from base.model.mapped_base_model import MappedBaseModel

class LoginModel(MappedBaseModel):
    
    Username: str
    Email: str        
    IsAdmin: bool
    LastIpAddress: str
    LastLoginDate: datetime
    
    key_map = {        
        "USERNAME"					    : "Username",
        "EMAIL"					        : "Email",         
        "IS_ADMIN"                      : "IsAdmin",
        "LAST_IP_ADDRESS"				: "LastIpAddress",
        "LAST_LOGIN_DATE_UTC"			: "LastLoginDate"        
    }
    
                