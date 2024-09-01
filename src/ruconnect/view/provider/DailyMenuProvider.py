from view.provider.Provider import Provider
from model import DailyMenu

class DailyMenuProvider(Provider):
    @staticmethod
    def label(obj: DailyMenu) -> str:
        return obj.id

    @staticmethod
    def info(obj: DailyMenu) -> tuple[tuple[str,str]]:
        return (
            ("Preço", obj.price),
            ("Data", obj.date),
            ("Almoço", ' '.join([edible.id for edible in obj.lunch])),
            ("Jantar", ' '.join([edible.id for edible in obj.dinner])),
        )
 