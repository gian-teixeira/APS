from view.provider.Provider import Provider
from model import Edible

class EdibleProvider(Provider):
    @staticmethod
    def label(obj: Edible) -> str:
        return obj.id

    @staticmethod
    def info(obj: Edible) -> tuple[tuple[str,str]]:
        return (
            ('Nome', obj.name),
            ('Calorias', obj.calories),
            ('Tipo', obj.type)
        )