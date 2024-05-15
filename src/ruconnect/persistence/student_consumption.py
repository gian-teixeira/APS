from persistence.persistence import Persistence

class StudentConsumptionPersistence(Persistence):
    def __init__(self):
        super().__init__("student_consumption")