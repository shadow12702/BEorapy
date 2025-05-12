# Description: Menu

from datetime import datetime
from base.domain.base_entity import BaseEntity

class Menu(BaseEntity):
    code: str
    name: str
    icon: str
    parent: str
    route: str
    prefix: str
    is_show: bool = True
    admin_site: bool  = True
    created_at: datetime = datetime.utcnow()
    updated_at: datetime = datetime.utcnow()
    
    key_map = {
        **BaseEntity.key_map,
        "MN_CODE" : "code",
        "MN_NAME"     : "name",
        "MN_ICON"    : "icon",
        "MN_PARENT"  : "parent",
        "MN_PREFIX"  : "prefix",
        "MN_LINK"    : "route",
        "MN_IS_SHOW" : "is_show",
        "MN_ADMIN_SITE": "admin_site",
        "CREATED_ON_UTC": "created_at",
        "UPDATED_ON_UTC": "updated_at"
    }

