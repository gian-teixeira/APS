from model.util import TypeException
from datetime import time

class Restaurant:
    __instance = None
    __price : float = 0
    __name : str = ""
    __operating_time : tuple[time,time] = (time(), time()) # TODO
    
    @classmethod
    def get_instance(cls):
        if cls.__instance is None:
            cls.__instance = cls()
        return cls.__instance
    
    def get_price(self) -> float:
        return self.__price
    
    def get_name(self) -> str:
        return self.__name
    
    def get_operating_time(self) -> tuple[time,time]:
        return self.__operating_time
    
    def set_price(self, 
                  price : float):
        TypeException.check_type(price, float)
        self.__price = price

    def set_name(self,
                 name : str):
        TypeException.check_type(name, str)
        self.__name = name
    
    