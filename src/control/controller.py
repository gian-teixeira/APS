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
        self.__persistence.create(obj)