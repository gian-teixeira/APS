from abc import ABC, abstractmethod
import json

class DAO(ABC):
    instance = None
    data = None

    def __init__(self):
        with open(self.filename, 'w+') as file:
            content = file.read()
            try: self.data = json.loads(content)
            except: self.data = dict()

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = cls()
        return cls.instance
    
    def close(self):
        json_data = json.dumps(self.data)
        with open(self.filename, 'w+') as file:
            file.write(json_data)
    
    @abstractmethod
    @property
    def filename(self) -> str: ...

    def read(self, id : str | None) -> dict | list[dict]:
        return self.data.get(id, None)

    def create(self, id : str, data : dict) -> None:
        if self.data.get(id, None) is not None: 
            raise Exception(f"{self.filename} : ID already present.")
        self.data[id] = data
    
    def update(self, id : str, data : dict) -> None:
        if self.data.get(id, None) is None:
            raise Exception(f"{self.filename} : ID not present.")
        return self.data[id]
    
    def delete(self, id : str) -> None:
        if self.data.get(id, None) is None:
            raise Exception(f"{self.filename} : ID not present.")
        del self.data[id]