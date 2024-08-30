from persistence.dao.DAO import DAO

class RestaurantDAO(DAO):
    @property
    def filename(self) -> str:
        return "restaurant"