from persistence.persistence import Persistence
from model.restaurant import Restaurant

class RestaurantPersistence(Persistence):
    def __init__(self):
        super().__init__("restaurant")
    