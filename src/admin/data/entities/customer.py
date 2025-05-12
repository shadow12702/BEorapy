from datetime import datetime
from base.domain.base_entity import BaseEntity

class Customer(BaseEntity):
    code: str
    name: str
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()

    key_map = {
        "CUS_CODE": "code",
        "CUS_NAME": "name",
        "CUS_CREATED_UTC": "created_at",
        "CUS_UPDATED_UTC": "updated_at",
    }   