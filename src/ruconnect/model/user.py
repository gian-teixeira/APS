from abc import ABC, abstractmethod

class User(ABC):
    def __init__(self, name : str, id : int, password : str):
        self.name = name
        self.id = id
        self.password = password
    
    def get_name(self) -> str:
        return self.name
    
    def set_name(self, name : str) -> None:
        self.name = name

    def get_id(self) -> int:
        return self.id
    
    def set_id(self, id : int) -> None:
        self.id = id
    
    def get_password(self) -> str:
        return self.password
    
    def set_password(self, password : str) -> None:
        self.password = password
    
    @abstractmethod
    def to_dict(self): ...
        
class Student(User):
    def __init__(self, name : str, id : int, password : str, credit : float):
        super().__init__(name, id, password)
        self.credit = credit
    
    def get_credit(self) -> float:
        return self.credit
    
    def set_credit(self, credit : float) -> None:
        self.credit = credit
    
    def to_dict(self) -> dict:
        return {
            "name" : self.get_name(),
            "id" : self.get_id(),
            "password" : self.get_password(),
            "credit" : self.get_credit()
        }
        
class Administrator(User):
    def __init__(self, name : str, id : int, password : str):
        super().__init__(name, id, password)
        
    def to_dict(self) -> dict:
        return {
            "name" : self.get_name(),
            "id" : self.get_id(),
            "password" : self.get_password()
        }