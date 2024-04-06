from persistence.persistence import Persistence
from model.edible import Edible

class EdiblePersistence(Persistence):
    def __init__(self):
        super().__init__("edible")