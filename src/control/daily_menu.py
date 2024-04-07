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
                       value : date):
        TypeException.check_type(value, date)
        return self.search({
            "date" : DateTime.date_string(value)
        })

    def delete_by_date(self, 
                       value : date):
        TypeException.check_type(value, date)
        self.__persistence.delete({
            "date" : DateTime.date_string(value)
        })

    def search_field(self):
        return ("Data", self.search_by_date)
    
    def delete_fuction(self, value):
        return self.delete_by_date