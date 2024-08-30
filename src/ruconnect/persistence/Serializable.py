from abc import ABC, abstractmethod

class Serializable(ABC):
    @abstractmethod
    def get_id(self) -> str: ...

    def __eq__(self, other):
        return self.get_id() == other.get_id()