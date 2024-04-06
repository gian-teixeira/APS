from persistence.persistence import Persistence
from model.daily_menu import DailyMenu

class DailyMenuPersistence(Persistence):
    def __init__(self):
        super().__init__("daily_menu")
