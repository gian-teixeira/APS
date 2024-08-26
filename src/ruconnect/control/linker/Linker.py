from abc import ABC, abstractmethod
from persistence import Serializable

class Linker(ABC):
    @abstractmethod
    def to_dict(self, obj : Serializable): ...

    @abstractmethod
    def to_object(self): ...

    @abstractmethod
    def get_persistence(self, obj : Serializable): ...