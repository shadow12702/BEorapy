from typing import Type, TypeVar, Dict


# Type variable for subclasses of BaseModel
T = TypeVar('T', bound='BaseEntity')

class BaseEntity:
    
    Id : int
    key_map = {'ID' : 'Id'}

    def __init__(self, **kwargs):
        # set attribute for model by mapping kwargs as key_map
        for key, model_attr in self.key_map.items():
            if key in kwargs:
                setattr(self, model_attr, kwargs.get(key))
            else:
                setattr(self, model_attr, kwargs.get(model_attr, None))
 
    # def to_dict(self) -> dict:
    #     """Convert the model instance to a dictionary with original keys."""
    #     output_dict = {}
    #     for _key, _attr in self.key_map.items():
    #             attr_value = getattr(self, _attr, None)
    #             output_dict[_key] = attr_value
                        
    #     # output_dict.update({attr: value for attr, value in self.__dict__.items() if attr not in reverse_key_map.values()})
    #     return output_dict

    # def _2dict(self):
    #     return self.__dict__
    
    def to_response(self) -> dict:
        out_dict = {}
        for k, v in self.key_map.items():
            attr = getattr(self, v, None)
            out_dict[v] = attr
        return out_dict
       
    @classmethod
    def from_dict(cls: Type[T], data: Dict) -> T:
        """
        Create an instance of the model by mapping from a key_map.

        Params:
            data: Dictionary with mapping names as keys and their values.
        
        Returns:
            An instance of cls with mapped key_map.
        """
        # Reverse the key_map to match dictionary keys to model attributes
        reverse_key_map = {v: k for k, v in cls.key_map.items()}
        mapped_data = {}
        for key, value in data.items():
            # Use the attribute name if it's in reverse_key_map; otherwise, keep the original key
            mapped_key = reverse_key_map.get(key.upper(), key)
            mapped_data[mapped_key] = value
        # Return an instance of the class with mapped data
        return cls(**mapped_data)
        
        
    @classmethod
    def empty(cls) -> 'BaseEntity':
        """Return an empty instance of the model with all attributes set to None"""
        return cls()

    @property
    def is_empty(self) -> bool:
        """Check if all atrributes of the instance are None"""
        for _, value in self.__dict__.items():
            if value is not None:
                return False
        return True
