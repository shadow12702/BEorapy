# 

from pydantic import BaseModel

class BaseModel(BaseModel):


    @property
    def is_empty(self):
        """
        Check if the model is empty.
        """
        return all(
            value in (None, "", [], {}, set())
            for value in self.dict().values()
        )
    