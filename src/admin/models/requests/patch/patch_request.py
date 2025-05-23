from typing import Optional
from pydantic import BaseModel

class PatchRequest(BaseModel):
    patch_id: int
    root: int
    db_version: str
    type: str
    format: str
    patch_type: str
    ru_fixed: Optional[str] = None
    mrp_fixed: Optional[str] = None
    description: Optional[str] = None