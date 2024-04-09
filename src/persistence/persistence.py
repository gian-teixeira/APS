from model.util import TypeException
from os import path
import json

class Persistence:
    __folder : str = "../data"

    def __init__(self, 
                 name : str):
        self.__name : str = name
        self.__data : dict
        self.load()
        
    def register(self, data : dict):
        TypeException.check_type(data, dict)

        self.load()

        self.__data["items"].append(data)
        self.save()

    def delete(self, data : dict):
        #TypeException.check_type(data, dict)

        self.load()

        targets = self.find(data)

        for target in targets:
            index = self.__data["items"].index(target)
            del self.__data["items"][index]

        self.save()
    
    def find(self, filter = None):
        self.load()

        if filter is None:
            return self.__data["items"]

        filter_items = set(filter.items())
        found = [item for item in self.__data["items"] 
                 if set(item.items()).issuperset(filter_items)]

        return found
    
    def load(self):
        if not path.isfile(self.filename()):
            self.create()
        
        try:
            filename : str = self.filename()
            with open(filename, "r") as file:
                self.__data = json.loads(file.read())
        except:
            raise IOError("Collection load : Icompatible file format")
    
    def save(self):
        try:
            filename : str = self.filename()
            with open(filename, "w") as file:
                file.write(json.dumps(self.__data))
        except IOError as io_error:
            print(io_error)
            raise IOError("Collection save : TODO")

    def filename(self) -> str:
        return f"{self.__folder}/{self.get_name()}.json"
    
    def create(self):
        filename : str = self.filename()
        with open(filename, "w+") as file:
            file.write(json.dumps({
                "items": []
            }))
    
    def __dict__(self):
        self.load()
        return self.__data

    def __getitem__(self, item):
        self.load()
        return self.__data[item]

    def get_name(self):
        return self.__name
    
    def get_data(self):
        return self.__data
    
    @classmethod
    def set_database_folder(cls, 
                            folder_path : str):
        if not path.isdir(folder_path):
            raise FileNotFoundError(f"folder {folder_path} not found")
        cls.__folder = folder_path

            