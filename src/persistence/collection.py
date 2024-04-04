from os import path
import json

class Collection:
    __folder : str = "../data"

    def __init__(self, 
                 name : str):
        self.__name : str = name
        self.__data : dict
        self.load()

    def load(self):
        if not path.isfile(self.__filename()):
            self.__create()
        
        try:
            filename : str = self.__filename()
            with open(filename, "r") as file:
                self.__data = json.loads(file.read())
        except:
            raise IOError("Collection load : TODO")
    
    def save(self):
        try:
            filename : str = self.__filename()
            with open(filename, "w") as file:
                file.write(json.dumps(self.__data))
        except:
            raise IOError("Collection save : TODO")
        
    def insert(self, data : dict):
        self.__data["items"].append(data)

    def find(self, filter : dict) -> list:
        found = list()

        for item in self.__data["items"]:
            valid = True
            for param in filter:
                if not param in item or filter[param] != item[param]:
                    valid = False
            if valid:
                found.append(item)

        return found

    def __filename(self) -> str:
        return f"{self.__folder}/{self.get_name()}.json"
    
    def __create(self):
        filename : str = self.__filename()
        with open(filename, "w+") as file:
            file.write(json.dumps({
                "items": []
            }))
    
    def __dict__(self):
        return self.__data

    def get_name(self):
        return self.__name
            