from persistence import DAO

class RestaurantPersistence(DAO):
    @property
    def filename(self) -> str:
        return "restaurant"