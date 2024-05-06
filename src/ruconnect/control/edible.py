from control.controller import Controller
from model.edible import Edible

class EdibleController(Controller):
    def __init__(self, persistence):
        super().__init__(persistence, Edible)

    def search(self, name):
        return super().search(None if name is None else {
            "name" : name
        })
    
    def delete(self, name):
        super().delete({
            "name" : name
        })
    
    def build_object(self, data):
        return Edible(*data.values())