from model.edible import Edible
from model.restaurant import Restaurant

class DailyMenu:
    def __init__(self, date):
        restaurant : Restaurant = Restaurant.get_instance()

        self.__price : float = restaurant.get_price()
        self.__lunch : list[Edible] = []
        self.__dinner : list[Edible] = []
        self.__date = date

    def lunch_add(self, edible):
        self.__lunch += edible

    def dinner_add(self, edible):
        self.__dinner += edible

    def lunch_erase(self):
        self.__lunch = []

    def dinner_erase(self):
        self.__dinner = []

    def get_lunch(self):
        return self.__lunch
    
    def get_dinner(self):
        return self.__dinner
    
    def get_price(self):
        return self.__price
    
    def set_price(self, price):
        self.__price = price

    def get_date(self):
        return self.__date
    
    def to_dict(self):
        return {
            "price": self.get_price(),
            "date": self.get_date(),
            "lunch": [edible.get_name() for edible in self.get_lunch()],
            "dinner": [edible.get_name() for edible in self.get_dinner()],
        }
    
    def attr_labels(self):
        return ("Preço", "Data", "Almoço", "Jantar")
    
    def __str__(self):
        return self.get_date()