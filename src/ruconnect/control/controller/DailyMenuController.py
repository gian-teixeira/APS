from control.controller.Controller import Controller
from control.linker.DailyMenuLinker import DailyMenuLinker

class DailyMenuController(Controller):
    @property
    def linker(self):
        return DailyMenuLinker()