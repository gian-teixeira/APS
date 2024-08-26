from persistence.edible import EdiblePersistence
from ruconnect.control.controller import Controller, EdibleController
from model.daily_menu import DailyMenu

from ruconnect.persistence import Serializable

class DailyMenuController(Controller):
    def __init__(self, persistence):
        super().__init__(persistence, DailyMenu)

    def build_object(self, data):
        edible_persistence = EdiblePersistence()
        edible_controller = EdibleController(edible_persistence)

        menu = DailyMenu(data["date"])
        menu.set_price(data["price"])
        
        for edible_name in data["lunch"]:
            edible = edible_controller.search(edible_name)
            menu.lunch_add(edible)

        for edible_name in data["dinner"]:
            edible = edible_controller.search(edible_name)
            menu.dinner_add(edible)

        return menu