from persistence.edible import EdiblePersistence
from control.edible import EdibleController
from control.controller import Controller
from model.daily_menu import DailyMenu

class DailyMenuController(Controller):
    def __init__(self, persistence):
        super().__init__(persistence, DailyMenu)
    
    def search_by_date(self, value):
        return self.search({
            "date" : value
        })

    def delete_by_date(self, value):
        self.persistence.delete({
            "date" : value
        })

    def build_object(self, data):
        edible_persistence = EdiblePersistence()
        edible_controller = EdibleController(edible_persistence)

        menu = DailyMenu(data["date"])
        menu.set_price(data["price"])
        
        for edible_name in data["lunch"]:
            edible = edible_controller.search_by_name(edible_name)
            menu.lunch_add(edible)

        for edible_name in data["dinner"]:
            edible = edible_controller.search_by_name(edible_name)
            menu.dinner_add(edible)

        return menu
            
        
