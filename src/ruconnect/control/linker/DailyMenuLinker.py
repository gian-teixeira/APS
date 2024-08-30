from control.linker.Linker import Linker
from control.controller.EdibleController import EdibleController
from model import DailyMenu
from persistence import DailyMenuDAO

class DailyMenuLinker(Linker):
    def to_dict(self, obj : DailyMenu) -> dict:
        return {
            "price": self.price,
            "date": self.date,
            "lunch": [edible.get_id() for edible in self.lunch],
            "dinner": [edible.get_id() for edible in self.dinner],
        }

    def to_object(self, data : dict) -> DailyMenu:
        edible_controller = EdibleController()
        
        menu = DailyMenu(data["date"])
        menu.price = data["price"]
        
        for edible_id in data["lunch"]:
            edible = edible_controller.read(edible_id)
            menu.lunch_add(edible)

        for edible_id in data["dinner"]:
            edible = edible_controller.read(edible_id)
            menu.dinner_add(edible)

        return menu
    
    def get_persistence(self):
        return DailyMenuDAO.get_instance()