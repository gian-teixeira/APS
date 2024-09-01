from abc import ABC, abstractmethod
from persistence import Serializable, DAO
from control.linker.Linker import Linker

class Controller(ABC):
    def create(self, obj : Serializable) -> None:
        persistence : DAO = self.linker.get_persistence()
        json_data = self.linker.to_dict(obj)
        persistence.create(obj.id, json_data)

    def read(self, id : str | None = None) -> None | list[Serializable]:
        persistence : DAO = self.linker.get_persistence()
        data = persistence.read(id)
        if data is None: return None
        objects = map(lambda tup : self.linker.to_object(tup[1]), data)
        return list(objects)
    
    def update(self, obj : Serializable) -> None:
        persistence : DAO = self.linker.get_persistence()
        json_data = self.linker.to_dict(obj)
        persistence.update(obj.id, json_data)
    
    def delete(self, obj : Serializable) -> None:
        persistence : DAO = self.linker.get_persistence()
        persistence.delete(obj.id)
        
    @property
    @abstractmethod
    def linker(self) -> Linker: ...