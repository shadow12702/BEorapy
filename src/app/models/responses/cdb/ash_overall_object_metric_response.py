# app/models/responses/cdb/ash_overall_metric_response.py

from pydantic import BaseModel

class AshOverallObjectMetricResponse(BaseModel):
    
    instance_name: str
    db_name: str
    pdb_name: str
    owner: str
    object_name: str
    percentage: float

    @classmethod
    def from_model(cls, model):
        return cls(
            instance_name = model.InstanceName,
            db_name = model.DbName,
            pdb_name = model.PdbName,
            owner = model.Owner,
            object_name = model.ObjectName,
            percentage = model.Percentage
        )
    