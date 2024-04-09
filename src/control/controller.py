from persistence.persistence import Persistence
from model.util import TypeException
from abc import ABC, abstractmethod

class Controller(dict, ABC):
    def __init__(self, persistence, cls):
        self.persistence = persistence
        self.__cls = cls

    def save(self, obj):
        print(self.__cls)
        TypeException.check_type(obj, self.__cls)
        self.persistence.register(obj.to_dict())

    def search(self, data = None):
        valid_info = self.persistence.find(data)
        return [self.build_object(info) for info in valid_info]
    
    def delete(self, data):
        self.persistence.delete(data)

    @abstractmethod
    def build_object(self, data): ...