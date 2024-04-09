from persistence.restaurant import RestaurantPersistence
from control.controller import Controller
from util.util import TypeException
from model.restaurant import Restaurant

class RestaurantController(Controller):
    def __init__(self, 
                 persistence : RestaurantPersistence):
        TypeException.check_type(persistence, RestaurantPersistence)
        super().__init__(persistence, Restaurant)

    def build_object(self, data):
        restaurant = Restaurant.get_instance()
        restaurant.set_name(data['name'])
        restaurant.set_operating_time(data['time'])
        restaurant.set_price(float(data['price']))

    def save(self):
        restaurant = Restaurant.get_instance()
        self.delete()
        super().save(restaurant)

    def search(self):
        return super().search(None)
    
    def delete(self):
        self.persistence.delete(None)