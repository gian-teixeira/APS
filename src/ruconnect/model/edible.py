class Edible:
    def __init__(self, name, type, calories):
        self.__name = name
        self.__type = type
        self.__calories = calories

    def get_name(self):
        return self.__name
    
    def get_type(self):
        return self.__type
    
    def get_calories(self):
        return self.__calories
    
    def __str__(self):
        return self.get_name()
     
    def to_dict(self):
        return {
            "name" : self.get_name(),
            "type" : self.get_type(),
            "calories" : self.get_calories()
        }
    
    def attr_labels(self):
        return ("Nome", "Tipo", "Calorias")