from edible import Edible
from restaurant import Restaurant
from util import TypeException

class DailyMenu:
    def __init__(self):
        restaurant : Restaurant = Restaurant.get_instance()

        self.__price : float = restaurant.get_price()
        self.__lunch : list[Edible] = []
        self.__dinner : list[Edible] = []

    @staticmethod
    def add_edible(target_list : list[Edible], 
                   edibles : list[Edible]):
        for edible in edibles:
            TypeException.check_type(edible, Edible)
        target_list += edibles

    def get_lunch(self) -> list[Edible]:
        return self.__lunch
    
    def get_dinner(self) -> list[Edible]:
        return self.__dinner
    
    def get_price(self) -> float:
        return self.__price