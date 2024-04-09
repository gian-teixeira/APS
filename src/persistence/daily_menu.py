from persistence.persistence import Persistence
from model.daily_menu import DailyMenu
from model.util import TypeException

class DailyMenuPersistence(Persistence):
    def __init__(self):
        super().__init__("daily_menu")

    def find(self, filter):
        self.load()

        if filter is None:
            return self.get_data()["items"]

        found = []
        for item in self.get_data()["items"]:
            if "price" in item and "price" in filter \
                and item["price"] != filter["price"]: continue
            found.append(item)

        return found
