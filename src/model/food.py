
from enum import Enum

class FoodType(Enum):
    MAIN_COURSE = "Prato principal"
    SIDE_DISH = "Acompanhamento"
    DESSERT = "Sobremesa"
    JUICE = "Suco"
    SALAD = "Salada"

class Food:
    def __init__(self, 
                 name : str,
                 type : str):
        self._name = name
        self._type = FoodType(type)

    @property
    def name(self):
        return self._name
    
    @property
    def type(self):
        return self._type
    
    @name.setter
    def name(self, 
             value : str):
        self.name = value
    
    @type.setter
    def type(self, 
             value : str):
        self.type = FoodType(value)