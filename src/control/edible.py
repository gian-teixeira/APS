from control.controller import Controller
from persistence.edible import EdiblePersistence
from persistence.edible import EdiblePersistence
from model.util import TypeException
from model.edible import Edible

class EdibleController(Controller):
    def __init__(self, 
                 persistence : EdiblePersistence):
        TypeException.check_type(persistence, EdiblePersistence)
        super().__init__(persistence, Edible)

    def search_by_name(self, 
                       name : str):
        TypeException.check_type(name, str)
        return self.search({
            "name" : name
        })
    
    def delete_by_name(self,
                       name : str):
        TypeException.check_type(name, str)
        self.delete({
            "name" : name
        })

    def search_field(self):
        return ("Nome", self.search_by_name)
    
    def delete_fuction(self):
        return self.delete_by_name