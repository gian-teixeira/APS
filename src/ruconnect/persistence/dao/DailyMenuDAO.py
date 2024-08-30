from persistence import DAO

class DailyMenuDAO(DAO):
    @property
    def filename(self) -> str:
        return "daily_menu"