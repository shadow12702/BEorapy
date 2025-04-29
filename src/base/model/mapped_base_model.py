# Description: MappedBaseModel

class MappedBaseModel:
    key_map = {}

    def __init__(self, **kwargs):
        if len(self.key_map) > 0:
            for key, attr in self.key_map.items():
                setattr(self, attr, kwargs.get(key))
        else:
            for k, v in kwargs.items():
                if isinstance(v, dict):
                    model_class = getattr(self.__class__, "__annotations__",{}).get(k)
                    if model_class:
                        v = model_class(**v) 
                    else:
                        v = MappedBaseModel(**v)
                setattr(self, k, v)

    def to_dict(self):
        return self.__dict__
    
    @classmethod
    def empty(cls):
        """Return an empty instance of the model with all attributes set to None"""
        return cls()

    @property
    def is_empty(self) -> bool:
        """Check if all atrributes of the instance are None"""
        for _, value in self.__dict__.items():
            if value is not None:
                return False
        return True