from control.linker.Linker import Linker
from model import Student
from persistence import StudentDAO

class StudentLinker(Linker):
    def to_dict(self, obj : Student) -> dict:
        return {
            "name": obj.name, 
            "cpf": obj.cpf, 
            "password": obj.password, 
            "credit": obj.credit,
        }

    def to_object(self, data : dict) -> Student:
        return Student(data["name"], data["cpf"], data["password"], data["credit"])
    
    def get_persistence(self):
        return StudentDAO.get_instance()