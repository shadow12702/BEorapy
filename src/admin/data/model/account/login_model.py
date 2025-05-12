# Description: LoginModel

from datetime import datetime
from typing import Optional

from base.model.base_model import BaseModel

class LoginModel(BaseModel):
    
    username: str
    email: Optional[str] = None
    is_admin: bool = False
    last_ip_address: str
    last_login_date: datetime
    
    
                