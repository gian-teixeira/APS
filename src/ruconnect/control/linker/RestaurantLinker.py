from control.linker.Linker import Linker
from model import Restaurant, Edible
from persistence import RestaurantDAO

class RestaurantLinker(Linker):
    def to_dict(self, obj : Edible) -> dict:
        return {
            "name" : obj.name,
            "price" : obj.price,
            "operating_time" : obj.operating_time,
        }        
    
    def to_object(self, data : dict) -> Restaurant:
        instance = Restaurant.get_instance()
        instance.price = data["price"]
        instance.name = data["price"]
        instance.operating_time = data["operating_time"]
        return instance
    
    def get_persistence(self):
        return RestaurantDAO.get_instance()
        