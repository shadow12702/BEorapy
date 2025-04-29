from datetime import datetime
from base.domain.base_entity import BaseEntity
from typing import Optional

class Patch(BaseEntity):
    patch_id: int
    root: int
    db_version: str
    type: str
    format: str
    patch_type: str
    ru_fixed: Optional[str] = None
    mrp_fixed: Optional[str] = None
    description: Optional[str] = None
    created_at: datetime

    key_map = {
        **BaseEntity.key_map,
        "DB_VERSION": "db_version",
        "TYPE": "type",
        "FORMAT": "format",
        "PATCH_ROOT": "root",
        "PATCH_ID": "patch_id",
        "PATCH_TYPE": "patch_type",
        "FIXED_IN_RU": "ru_fixed",
        "FIXED_IN_MRP": "mrp_fixed",
        "DESCRIPTION": "description",
        "CREATED_UTC": "created_at", 
    }
