class MealRegister:
    def __init__(self, student, menu, id):
        self.student = student
        self.menu = menu
        self.id = id

    def to_dict(self):
        return {
            "student": self.student,
            "menu": self.menu,
            "id": self.id
        }