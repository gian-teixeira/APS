from control.controller import Controller
from model.user import Student
from model.user import Administrator
from abc import ABC, abstractmethod

class UserController(Controller, ABC):
    def search(self, id):
        return super().search(None if id is None else {
            "id" : id
        })
    
    def delete(self, id):
        super().delete({
            "id" : id
        })
    
    def build_object(self, data):
        return Student(*data.values())

class StudentController(UserController):
    def __init__(self, persistence):
        super().__init__(persistence, Student)

    def build_object(self, data):
        return Student(*data.values())

class AdministratorController(UserController):
    def __init__(self, persistence):
        super().__init__(persistence, Administrator)

    def build_object(self, data):
        return Administrator(*data.values())