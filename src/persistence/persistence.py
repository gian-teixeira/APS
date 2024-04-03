from model.restaurant import Restaurant
from model.edible import Edible
from model.util import TypeException

class Persistence:
    __database = None

    def __init__(self,
                 cls : type,
                 collection : str):
        self.__cls = cls
        self.__collection = collection

    def create(self, obj : object):
        TypeException.check_type(obj, self.get_cls())
        # database[self.get_collection()].insert_one(obj.__dict__)

    def search(self, obj : object): ...

    def delete(self, obj : object): ...

    def get_cls(self) -> type:
        return self.__cls
    
    def get_collection(self) -> str:
        return self.__collection

class RestaurantPersistence(Persistence):
    def __init__(self):
        super().__init__(Restaurant, "restaurant")

class EdiblePersistence(Persistence):
    def __init__(self):
        super().__init__(Edible, "edible")