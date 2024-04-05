from model.util import TypeException
from persistence.collection import Collection
import json

class Persistence:
    def __init__(self,
                 cls : type,
                 collection : str):
        self.__cls = cls
        self.__collection = Collection(collection)

    def register(self, 
                 obj : object):
        self.__collection.insert(obj.__dict__)

    def search(self, data : dict) -> object:
        self.__collection.find(data)

    def delete(self, data : dict):
        self.__collection.delete(data)

    def get_cls(self) -> type:
        return self.__cls
    
    def get_collection(self) -> Collection:
        return self.__collection