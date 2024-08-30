from abc import ABC, abstractmethod
from persistence import Serializable

class User(Serializable):
    def __init__(self, name : str, cpf : int, password : str):
        self.name = name
        self.cpf = cpf
        self.password = password
    
    @property
    def id(self):
        return self.cpf
        
class Student(User):
    def __init__(self, name : str, cpf : int, password : str, credit : float):
        super().__init__(name, cpf, password)
        self.credit = credit
        
class Administrator(User):
    def __init__(self, name : str, cpf : int, password : str):
        super().__init__(name, cpf, password)