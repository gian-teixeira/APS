from control.controller import Controller
from model.meal_register import MealRegister

class MealRegisterController(Controller):
    def __init__(self, persistence):
        super().__init__(persistence, MealRegister)
    
    def search(self, id):
        return super().search(None if name is None else {
            "id" : id
        })
    
    def delete(self, id):
        super().delete({
            "id" : id
        })
    
    def build_object(self, data):
        return MealRegister(*data.values())