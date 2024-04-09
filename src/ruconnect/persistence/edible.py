from persistence.persistence import Persistence

class EdiblePersistence(Persistence):
    def __init__(self):
        super().__init__("edible")