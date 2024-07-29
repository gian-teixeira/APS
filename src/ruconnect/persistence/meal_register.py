from persistence.persistence import Persistence

class MealRegisterPersistence(Persistence):
    def __init__(self):
        super().__init__("meal_register")