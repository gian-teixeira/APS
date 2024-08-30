from abc import ABC, abstractmethod
from persistence import Serializable, DAO
from control.linker.Linker import Linker

class Controller(ABC):
    def create(self, obj : Serializable) -> None:
        persistence : DAO = self.linker.get_persistence()
        json_data = self.linker.to_dict(obj)
        persistence.create(obj.id, json_data)

    def read(self, id : str | None) -> None | Serializable | list[Serializable]:
        persistence : DAO = self.linker.get_persistence()
        data = persistence.read(id)
        if data is None: return None
        if isinstance(data, list): 
            objects = map(self.linker.to_object, data)
            return list(objects)
        return self.linker.to_object(data)
    
    def update(self, obj : Serializable) -> None:
        persistence : DAO = self.linker.get_persistence()
        json_data = self.linker.to_dict(obj)
        data = persistence.update(obj.id, json_data)
        objects = map(self.linker.to_object, data)
        return list(objects)
    
    def delete(self, obj : Serializable) -> None:
        persistence : DAO = self.linker.get_persistence()
        persistence.delete(obj.id)
        
    @property
    @abstractmethod
    def linker(self) -> Linker: ...