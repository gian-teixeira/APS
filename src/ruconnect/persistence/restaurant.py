from persistence.persistence import Persistence

class RestaurantPersistence(Persistence):
    def __init__(self):
        super().__init__("restaurant")