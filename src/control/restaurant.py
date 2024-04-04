from persistence.restaurant import RestaurantPersistence
from control.controller import Controller
from model.util import TypeException
from model.restaurant import Restaurant

class RestaurantController(Controller):
    def __init__(self, 
                 persistence : RestaurantPersistence):
        TypeException.check_type(persistence, RestaurantPersistence)
        super().__init__(persistence, Restaurant)