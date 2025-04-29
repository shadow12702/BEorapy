# Description: Config

from datetime import datetime
from base.domain.base_entity import BaseEntity

class Config(BaseEntity):
    type : str
    key : str
    value: str
    is_locked: int
    created_at : datetime
    last_updated : datetime
    
    key_map = {
        **BaseEntity.key_map,
        "CF_TYPE" : "type",
        "CF_KEY" : "key",
        "CF_VALUE" : "value",
        "CF_IS_LOCKED" : "is_locked",
        "CREATED_ON_UTC" : "created_at",
        "LAST_CHANGED" : "last_updated",
    }

