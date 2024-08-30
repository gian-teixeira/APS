from control.controller.Controller import Controller
from control.linker.EdibleLinker import EdibleLinker

class EdibleController(Controller):
    @property
    def linker(self):
        return EdibleLinker()