#Description: DbContextConfigModel
# 
from base.model.mapped_base_model import MappedBaseModel

class DbContextConfigModel(MappedBaseModel):
    MinPoolSize: int
    MaxPoolSize: int
    Increment: int
    Username: str
    Password: str
    Dsn: str
