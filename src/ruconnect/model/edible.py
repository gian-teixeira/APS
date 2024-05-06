from model.edible_type import EdibleType
import typing

class Edible:
    def __init__(self, name : str, type : EdibleType, calories : int):
        self.__name = name
        self.__type = type
        self.__calories = calories

    def get_name(self) -> str:
        return self.__name
    
    def get_type(self) -> EdibleType:
        return self.__type
    
    def get_calories(self) -> int:
        return self.__calories
    
    def __str__(self) -> str:
        return self.get_name()
     
    def to_dict(self) -> dict:
        return {
            "name" : self.get_name(),
            "type" : self.get_type(),
            "calories" : self.get_calories()
        }
    
    def attr_labels(self) -> tuple:
        return ("Nome", "Tipo", "Calorias")