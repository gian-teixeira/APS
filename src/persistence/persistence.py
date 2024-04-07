from model.util import TypeException
from os import path
import json

class Persistence:
    __folder : str = "../data"

    def __init__(self, 
                 name : str):
        self.__name : str = name
        self.__data : dict
        self.__load()
        
    def register(self, data : dict):
        TypeException.check_type(data, dict)

        self.__load()

        filter_items = set(data.items())
        found = [item for item in self.__data["items"] 
                 if set(item.items()).issuperset(filter_items)]
        
        if len(found): raise Exception

        self.__data["items"].append(data)
        self.__save()

    def delete(self, data : dict):
        TypeException.check_type(data, dict)

        self.__load()

        targets = self.find(data)

        for target in targets:
            index = self.__data["items"].index(target)
            del self.__data["items"][index]

        self.__save()
    
    # TODO : pesquisar com substring
    def find(self, filter : dict) -> list[dict]:
        TypeException.check_type(filter, dict)

        self.__load()

        filter_items = set(filter.items())
        found = [item for item in self.__data["items"] 
                 if set(item.items()).issuperset(filter_items)]

        return found
    
    def __load(self):
        if not path.isfile(self.__filename()):
            self.__create()
        
        try:
            filename : str = self.__filename()
            with open(filename, "r") as file:
                self.__data = json.loads(file.read())
        except:
            raise IOError("Collection load : TODO")
    
    def __save(self):
        try:
            filename : str = self.__filename()
            with open(filename, "w") as file:
                file.write(json.dumps(self.__data))
        except:
            raise IOError("Collection save : TODO")

    def __filename(self) -> str:
        return f"{self.__folder}/{self.get_name()}.json"
    
    def __create(self):
        filename : str = self.__filename()
        with open(filename, "w+") as file:
            file.write(json.dumps({
                "items": []
            }))
    
    def __dict__(self):
        self.__load()
        return self.__data

    def __getitem__(self, item):
        self.__load()
        return self.__data[item]

    def get_name(self):
        return self.__name
    
    @classmethod
    def set_database_folder(cls, 
                            folder_path : str):
        if not path.isdir(folder_path):
            raise FileNotFoundError(f"folder {folder_path} not found")
        cls.__folder = folder_path

            