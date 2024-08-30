from control.controller.Controller import Controller
from control.linker.StudentConsumptionLinker import StudentConsumptionLinker

class StudentConsumption(Controller):
    @property
    def linker(self):
        return StudentConsumption()