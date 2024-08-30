from model.Edible import Edible
from model.Restaurant import Restaurant
from persistence import Serializable

class DailyMenu(Serializable):
    def __init__(self, date):
        restaurant = Restaurant.get_instance()
        self.price = restaurant.price
        self.lunch = []
        self.dinner = []
        self.date = date

    @property
    def id(self) -> str:
        return self.date

    def lunch_add(self, edible):
        self.lunch += edible

    def dinner_add(self, edible):
        self.dinner += edible

    def lunch_erase(self):
        self.lunch = []

    def dinner_erase(self):
        self.dinner = []