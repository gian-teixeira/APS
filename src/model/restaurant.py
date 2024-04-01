from datetime import time
from enum import Enum
import json
from meal import Meal
from daily_data import DailyData

class Weekday(Enum): 
    SUNDAY = 1
    MONDAY = 2
    TUESDAY = 3
    WEDNESDAY = 4
    THURSDAY = 5
    FRIDAY = 6
    SATURDAY = 7

class Period(Enum):
    LUNCH = 1
    DINNER = 2

class Storable:
    @property
    def id(self): ...
    def json(self): ...

class Persistance:
    @staticmethod
    def save(obj : Storable): 
        print(obj.id)
        print(obj.json())

    @staticmethod
    def setter(setter):
        def wrapper(*args, **kwargs):
            Persistance.save(args[0])
            setter(*args, **kwargs)
        return wrapper
    
class Restaurant(Storable):
    _instance = None
    _operating_time = None
    _phone = None
    _email = None
    _credit_price = None
    _week_meals = dict()
    
    def __init__(self):
        self._week_meals = {
            day : {
                period : Meal()
                for period in Period
            }
            for day in Weekday
        }

    def json(self) -> str:
        return json.dumps({
            "operating_time": self.operating_time,
            "phone": self.phone,
            "email": self.email,
            "credit_price": self._credit_price
        })

    @classmethod
    def instance(cls):
        if cls._instance is None: 
            cls._instance = Restaurant()
        return cls._instance

    # GETTERS

    def get_meal(self, 
                 day : Weekday,
                 period : Period):
        return self.week_meals[day][period] 
    
    @property
    def operating_time(self):
        return self._operating_time

    @property
    def phone(self):
        return self._phone
    
    @property
    def email(self):
        return self._email
    
    @property
    def credit_price(self):
        return self._credit_price
    
    @property
    def week_meals(self):
        return self._week_meals
    
    # SETTERS
     
    @Persistance.setter
    def set_meal(self, 
                   day : Weekday,
                   period : Period,
                   meal : Meal):
        self.week_meals[day][period] = meal
    
    @operating_time.setter
    @Persistance.setter
    def operating_time(self, 
                       value : tuple[time]):
        self._operating_time = value

    @phone.setter
    @Persistance.setter
    def phone(self, 
              value : int):
        self._phone = value
        
    @email.setter
    @Persistance.setter
    def email(self, 
              value : str):
        self._email = value
    
    @credit_price.setter
    @Persistance.setter
    def credit_price(self, 
                     value : float):
        self._credit_price = value

class RestaurantPersistance(Storable):
    def __init__(self, 
                 target : Restaurant):
        self.target = target

    def json(self) -> str:
        return json.dumps({
            "operating_time": self.target.operating_time,
            "phone": self.target.phone,
            "email": self.target.email,
            "credit_price": self.target._credit_price
        })
    

if __name__ == "__main__":
    rest = Restaurant.instance()