from control.controller.Controller import Controller
from control.linker.StudentConsumptionLinker import StudentConsumptionLinker

class StudentConsumptionController(Controller):
    @property
    def linker(self):
        return StudentConsumptionLinker()