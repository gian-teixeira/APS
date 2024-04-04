from model.restaurant import Restaurant
from model.edible import Edible
from model.util import TypeException
import json

class Persistence:
    def __new__(cls):
        super().__new__(cls)
        cls.__folder__ = "../data"
        cls.__collections__ = {}

    def __init__(self,
                 cls : type,
                 collection : str):
        self.__cls = cls
        self.__collection = collection

    @classmethod
    def __create_collection(cls, collection):
        cls.__database = json.loads(cls.__folder__)
        filename = f"{cls.__folder__}/{collection}.json"
        with open(filename, "w+") as file:
            file.write(json.dumps({
                "items": []
            }))

    @classmethod
    def __activate_collection__(cls, collection):
        file = open(f"{cls.__folder__}/{collection}.json", "r")


    @classmethod
    def __save_active_collection(cls, ):
        pass

    def register(self, 
                 obj : object):
        TypeException.check_type(obj, self.get_cls())

        if not self.get_collection() in Persistence.__collections__:
            Persistence.__create_collection(self.get_collection())

        filename = f"{self.__folder__}/{self.get_collection()}.json"
        with open(filename, "w+") as file:
            collection = json.loads(file.read())
            collection["items"].append(obj.__dict__)
            file.write(json.dumps(collection))

    def search(self, data : dict) -> object:
        pass

    def delete(self, data : dict):
        register = self.search(data)

    def get_cls(self) -> type:
        return self.__cls
    
    def get_collection(self) -> str:
        return self.__collection