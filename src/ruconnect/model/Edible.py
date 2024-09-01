from model.EdibleType import EdibleType
from persistence import Serializable

class Edible(Serializable):
    def __init__(self, name : str, type : EdibleType, calories : int):
        self.name = name
        self.type = type
        self.calories = calories

    @property
    def id(self) -> str:
        return self.name
     