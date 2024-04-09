from model.edible_type import EdibleType
from util.util import TypeException

class Edible:
    def __init__(self, 
                 name : str,
                 type : str,
                 calories : int):
        TypeException.check_type(name, str)
        TypeException.check_type(type, str)
        TypeException.check_type(calories, int)

        self.__name = name
        self.__type = type
        self.__calories = calories

    def get_name(self) -> str:
        return self.__name
    
    def get_type(self) -> str:
        return self.__type
    
    def get_calories(self) -> int:
        return self.__calories
    
    def __str__(self) -> str:
        return self.get_name()
     
    def to_dict(self):
        return {
            "name" : self.get_name(),
            "type" : self.get_type(),
            "calories" : self.get_calories()
        }
    
    def attr_labels(self):
        return ("Nome", "Tipo", "Calorias")