from os import path
import json
import re

class Persistence:
    __folder : str = "../data"

    def __init__(self, 
                 name : str):
        self.__name : str = name
        self.data : dict
        self.load()
        
    def register(self, data : dict):
        self.load()

        self.data["items"].append(data)
        self.save()

    def delete(self, data : dict):
        self.load()

        targets = self.find(data)

        for target in targets:
            index = self.data["items"].index(target)
            del self.data["items"][index]

        self.save()
    
    def find(self, specs : dict | None = None):
        self.load()

        if specs is None:
            return self.data["items"]
        
        found = []
        
        for item in self.data["items"]:
            valid = True
            for key in specs:
                value = str(specs[key]).lower()
                if key in item and re.search(f'^{value}.*', str(item[key]).lower()):
                    continue
                valid = False
                break
            if valid:
                found.append(item)

        return found
    
    def load(self):
        if not path.isfile(self.filename()):
            self.create()
        
        try:
            filename : str = self.filename()
            with open(filename, "r") as file:
                self.data = json.loads(file.read())
        except:
            raise IOError("Collection load : Icompatible file format")
    
    def save(self):
        try:
            filename : str = self.filename()
            with open(filename, "w") as file:
                file.write(json.dumps(self.data))
        except IOError as io_error:
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
        return self.data

    def __getitem__(self, item):
        self.load()
        return self.data[item]

    def get_name(self):
        return self.__name
    
    def get_data(self):
        return self.data
    
    @classmethod
    def set_database_folder(cls, 
                            folder_path : str):
        if not path.isdir(folder_path):
            raise FileNotFoundError(f"folder {folder_path} not found")
        cls.__folder = folder_path

            