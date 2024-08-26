from abc import ABC, abstractmethod
from ruconnect.persistence.Serializable import Serializable

class Controller(ABC):
    def save(self, obj : Serializable) -> None:
        persistence = self.linker.get_persistence()
        persistence.save(obj.json())

    def search(self, obj : Serializable) -> list[Serializable]:
        persistence = self.linker.get_persistence()
        data = persistence.search(obj.get_id())
        objects = map(self.linker.to_object, data)
        return list(objects)
    
    def delete(self, obj : Serializable) -> None:
        persistence = self.linker.get_persistence()
        persistence.delete(obj.get_id())

    def get_linker(self):
        return self.linker