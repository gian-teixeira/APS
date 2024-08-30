from abc import ABC, abstractmethod

class Serializable(ABC):
    @property
    @abstractmethod
    def id(self) -> str: ...
    
    def __eq__(self, other):
        return self.id() == other.get_id()