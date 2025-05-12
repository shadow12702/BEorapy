#app/data/models/awr_repo_info/awr_info_customer_model.py 

from datetime import datetime
from base.model.base_model import BaseModel

class AwrInfoCustomerResponse(BaseModel):    
    customer_code: str
    dbid: int = 0
    database_name: str
    version: str
    is_cdb: bool = False
    begin_snap: int
    begin_time: datetime
    end_snap: int
    end_time: datetime
    is_rac: bool = False
    is_exa: bool = False
    block_size: int

    @classmethod
    def from_model(cls, model):
        return cls(
            customer_code= model.customer_code,
            dbid=model.dbid,
            database_name=model.database_name,
            version=model.version,
            is_cdb=model.is_cdb.lower() == "yes",
            begin_snap=model.begin_snap,
            begin_time=model.begin_time,
            end_snap=model.end_snap,
            end_time=model.end_time,
            is_rac=model.is_rac.lower() == "yes",
            is_exa=model.is_exa == 0,
            block_size=model.block_size
        )
    
