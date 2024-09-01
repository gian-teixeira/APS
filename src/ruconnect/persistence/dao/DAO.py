from abc import ABC, abstractmethod
import json
import os

class DAO(ABC):
    instance = None
    data = None

    def __init__(self):
        self.load()

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = cls()
        return cls.instance
    
    @property
    @abstractmethod
    def filename(self) -> str: ...
    
    def save(self):
        json_data = json.dumps(self.data)
        with open(f"data/{self.filename}.json", 'w+') as file:
            file.write(json_data)

    def load(self):
        try:
            with open(f"data/{self.filename}.json", 'r') as file:
                self.data = json.load(file)
        except: 
            self.data = dict()


    def read(self, id : str | None = None) -> None | list[tuple[str,dict]]:
        self.load()
        if id is None:
            return list(self.data.items())
        if not id in self.data: return None
        return [(id, self.data.get(id))]

    def create(self, id : str, data : dict) -> None:
        self.load()
        if id in self.data:
            raise Exception(f"{self.filename} : ID already present.")
        self.data[id] = data
        self.save()
    
    def update(self, id : str, data : dict) -> None:
        self.load()
        if not id in self.data:
            raise Exception(f"{self.filename} : ID not present.")
        self.data[id] = data
        self.save()
    
    def delete(self, id : str) -> None:
        self.load()
        if not id in self.data:
            raise Exception("Delete : ID not present.")
        del self.data[id]
        self.save()