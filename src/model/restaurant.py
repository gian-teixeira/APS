from model.util import TypeException
from datetime import time

class Restaurant:
    __instance = None
    __price = 0
    __name = ""
    __operating_time = ("", "")
    
    @classmethod
    def get_instance(cls):
        if cls.__instance is None:
            cls.__instance = cls()
        return cls.__instance
    
    def get_price(self):
        return self.__price
    
    def get_name(self):
        return self.__name
    
    def get_operating_time(self):
        return self.__operating_time
    
    def set_price(self, 
                  price : float):
        TypeException.check_type(price, float)
        self.__price = price

    def set_name(self,
                 name : str):
        TypeException.check_type(name, str)
        self.__name = name
    
    def set_operating_time(self,
                           operating_time):
        #TypeException.check_type(operating_time, tuple[time,time])
        self.__operating_time = operating_time

    def to_dict(self):
        return {
            "name" : self.get_name(),
            "time" : " | ".join(self.get_operating_time()),
            "price" : self.get_price()
        }
    
    def attr_labels(self):
        return ("Nome", "Tempo de Funcionamento", "Preço")