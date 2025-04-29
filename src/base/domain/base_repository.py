from abc import ABC, abstractmethod
from data.db_context import DbContext

class BaseRepository(ABC):
    
    def __init__(self, db_context: DbContext) -> None:
        self.db_context = db_context

    @abstractmethod
    def get_by_id(self, id):
        pass
    @abstractmethod
    def get_all(self):
        pass
    @abstractmethod
    def add(self, entity):
        pass
    @abstractmethod
    def update(self, id, entity):
        pass
    @abstractmethod
    def delete(self, id):
        pass

    