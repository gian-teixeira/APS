from model.edible import Edible
from model.restaurant import Restaurant

class DailyMenu:
    def __init__(self, date):
        restaurant = Restaurant.get_instance()

        self.price = restaurant.get_price()
        self.lunch = []
        self.dinner = []
        self.date = date

    def lunch_add(self, edible):
        self.lunch += edible

    def dinner_add(self, edible):
        self.dinner += edible

    def lunch_erase(self):
        self.lunch = []

    def dinner_erase(self):
        self.dinner = []

    def get_lunch(self):
        return self.lunch
    
    def get_dinner(self):
        return self.dinner
    
    def get_price(self):
        return self.price
    
    def set_price(self, price):
        self.price = price

    def get_date(self):
        return self.date
    
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