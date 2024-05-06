from persistence.persistence import Persistence

class DailyMenuPersistence(Persistence):
    def __init__(self):
        super().__init__("daily_menu")
