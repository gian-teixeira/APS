from persistence.daily_menu import DailyMenuPersistence
from control.controller import Controller
from model.util import DateTime, TypeException
from model.daily_menu import DailyMenu
from datetime import date

class DailyMenuController(Controller):
    def __init__(self, 
                 persistence : DailyMenuPersistence):
        TypeException.check_type(persistence, DailyMenuPersistence)
        super().__init__(persistence, DailyMenu)
    
    def search_by_date(self, 
                       date : date) -> object:
        data = {
            "date" : DateTime.date_string(date)
        }
        self.__persistence.search(data)

    def delete_by_date(self, 
                       date : date):
        pass
