
class Food:
    def __init__(self, 
                 name : str):
        self._name = name

    @property
    def name(self):
        return self._name
        
    @name.setter
    def name(self, 
             value : str):
        
        
food.name = value

