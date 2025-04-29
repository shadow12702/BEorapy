#Description: JwtAuthConfigModel
# 
from base.model.mapped_base_model import MappedBaseModel


class JwtAuthConfigModel(MappedBaseModel):
    JwtAuthKey :str
    Algorithm: str
    TokenExpireMinutes: int
    RefreshExpireDays: int