from persistence.persistence import Persistence

class StudentPersistence(Persistence):
    def __init__(self):
        super().__init__("student")

class AdministratorPersistence(Persistence):
    def __init__(self):
        super().__init__("administrator")