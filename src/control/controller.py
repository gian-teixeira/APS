from persistence.persistence import Persistence
from model.util import TypeException

class Controller(dict):
    def __init__(self, 
                 persistence : Persistence,
                 cls : type):
        self.__persistence = persistence
        self.__cls = cls

    def save(self, 
             obj):
        TypeException.check_type(obj, self.__cls)
        self.__persistence.register(obj.to_dict())

    def search(self,
               data : dict = {}):
        TypeException.check_type(data, dict)
        valid_info = self.__persistence.find(data)
        return [self.__cls(*info.values()) for info in valid_info]
    
    def delete(self,
               data : dict):
        self.__persistence.delete(data)
    
    def search_field(self): ...
    def register_fields(self): ...
    def delete_function(self): ...