from base.domain.base_entity import BaseEntity

class BestPractice(BaseEntity):
    Id: int
    DbVersion: str
    Parameter: str
    ParamDefaultValue: str
    ParamRecommendValue: str
    ForRacOnly: int
    Notes: str
    CreatedUtc: str 
    UpdatedUtc: str  

    key_map = {
        **BaseEntity.key_map,        
        "BP_DB_VERSION": "DbVersion",
        "BP_PARAMETER": "Parameter",
        "BP_PARAM_DEFAULT_VALUE": "ParamDefaultValue",
        "BP_PARAM_RECOMMEND_VALUE": "ParamRecommendValue",
        "BP_FOR_RAC_ONLY": "ForRacOnly",
        "BP_NOTES": "Notes",
        "CREATED_UTC": "CreatedUtc",
        "UPDATED_UTC": "UpdatedUtc",
    }
