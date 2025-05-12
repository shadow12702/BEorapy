# app/models/responses/cdb/ash_overall_metric_response.py

from pydantic import BaseModel

class AshOverallMetricResponse(BaseModel):
    
    instance_name: str
    db_name: str
    pdb_name: str
    metric_value: str
    percentage: float

    @classmethod
    def from_model(cls, model):
        return cls(
            instance_name = model.InstanceName,
            db_name = model.DbName,
            pdb_name = model.PdbName,
            metric_value = model.MetricValue,
            percentage = model.Percentage
        )
    