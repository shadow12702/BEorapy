# 

from numpy import int64
from base.model.mapped_base_model import MappedBaseModel


class AwrInfoCustomerModel(MappedBaseModel):    

    Dbid: int64
    DbName: str
    
    key_map = {
        "DBID" : "Dbid",
        "DB_NAME" : "DbName",
    }