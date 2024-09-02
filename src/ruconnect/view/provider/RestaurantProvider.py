from view.provider.Provider import Provider
from model import Restaurant

class RestaurantProvider(Provider):
    @staticmethod
    def label(obj: Restaurant) -> str:
        return obj.name

    @staticmethod
    def info(obj: Restaurant) -> tuple[tuple[str,str]]:
        return (
            ("Nome",  obj.name),
            ("Preço",  obj.price),
            ("Horário de funcionamento",  ' | '.join(obj.operating_time)),
        )