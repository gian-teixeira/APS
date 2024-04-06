from persistence.persistence import Persistence
from model.util import TypeException

class Controller(dict):
    def __init__(self, 
                 persistence : Persistence,
                 cls : type):
        self.__persistence = persistence
        self.__cls = cls

    def save(self, 
             obj : object):
        TypeException.check_type(obj, self.__cls)

        self.__persistence.register(obj.__dict__)

    def search(self,
               data : dict):
        TypeException.check_type(data, dict)
        
        valid_info = self.__persistence.find(data)
        
        return [self.__cls(*info.values()) for info in valid_info]