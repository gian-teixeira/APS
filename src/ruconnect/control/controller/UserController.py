from control.controller.Controller import Controller
from control.linker.AdministratorLinker import AdministratorLinker
from control.linker.StudentLinker import StudentLinker
from model import Student, Administrator
from abc import ABC, abstractmethod

class UserController(Controller, ABC):
    @property
    def linker(self): ...

class StudentController(UserController):
    @property
    def linker(self):
        return StudentLinker()

class AdministratorController(UserController):
    @property
    def linker(self):
        return AdministratorLinker()