from datetime import datetime
from base.domain.base_entity import BaseEntity

class Customer(BaseEntity):
    Code: str
    Name: str
    CreatedUtc: datetime = datetime.now()
    UpdatedUtc: datetime = datetime.now()

    key_map = {
        "CUS_CODE": "Code",
        "CUS_NAME": "Name",
        "CUS_CREATED_UTC": "CreatedUtc",
        "CUS_UPDATED_UTC": "UpdatedUtc",
    }   