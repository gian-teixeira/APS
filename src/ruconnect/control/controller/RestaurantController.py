from control.controller.Controller import Controller
from control.linker.RestaurantLinker import RestaurantLinker

class RestaurantController(Controller):
    @property
    def linker(self):
        return RestaurantController()
