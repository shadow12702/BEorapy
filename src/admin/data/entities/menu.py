# Description: Menu

from datetime import datetime
from base.domain.base_entity import BaseEntity

class Menu(BaseEntity):
    Code: str
    Name: str
    Icon: str
    Parent: str
    Route: str
    IsShow: bool = True
    AdminSite: bool  = True
    CreatedOnUtc: datetime = datetime.utcnow()
    UpdatedOnUtc: datetime = datetime.utcnow()
    
    key_map = {
        **BaseEntity.key_map,
        "MN_CODE" : "Code",
        "MN_NAME"     : "Name",
        "MN_ICON"    : "Icon",
        "MN_PARENT"  : "Parent",
        "MN_LINK"    : "Route",
        "MN_IS_SHOW" : "IsShow",
        "MN_ADMIN_SITE": "AdminSite",
        "CREATED_ON_UTC": "CreatedOnUtc",
        "UPDATED_ON_UTC": "UpdatedOnUtc"
    }

