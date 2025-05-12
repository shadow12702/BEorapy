from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class AwrRepoInfoResponse(BaseModel):
    customer_code: str
    customer_name: str
    version: str 
    dbid: int
    db_name: str
    is_cdb: bool = False
    pdb_dbid: int 
    pdb_name: str 
    end_snap: Optional[int] = None
    end_time: Optional[datetime] = None
    is_rac: bool = False
    is_exa: bool = False
    block_size: int

    @classmethod
    def from_model(cls, model):
        return cls(
            customer_code=model.customer_code,
            customer_name=model.customer_name,
            version=model.version,
            dbid=model.dbid,
            db_name=model.database_name,
            is_cdb=model.is_cdb.lower() == "yes",
            pdb_dbid=model.pdb_dbid,
            pdb_name=model.pdb_name,
            end_snap=model.end_snap,
            end_time=model.end_time,
            is_rac=model.is_rac.lower() == "yes",
            is_exa=model.is_exa == 0,
            block_size=model.block_size
        )