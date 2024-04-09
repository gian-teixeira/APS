from control.controller import Controller
from persistence.edible import EdiblePersistence
from persistence.edible import EdiblePersistence
from util.util import TypeException
from model.edible import Edible

class EdibleController(Controller):
    def __init__(self, persistence):
        TypeException.check_type(persistence, EdiblePersistence)
        super().__init__(persistence, Edible)

    def search_by_name(self, name):
        TypeException.check_type(name, str)
        return self.search({
            "name" : name
        })
    
    def delete_by_name(self, name):
        TypeException.check_type(name, str)
        self.delete({
            "name" : name
        })

    def build_object(self, data):
        return Edible(*data.values())