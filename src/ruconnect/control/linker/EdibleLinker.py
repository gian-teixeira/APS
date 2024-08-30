from control.linker.Linker import Linker
from model import Edible
from persistence import EdibleDAO

class EdibleLinker(Linker):
    def to_dict(self, obj : Edible) -> dict:
        return {
            "name": obj.name,
            "type": obj.type,
            "calories": obj.calories,
        }

    def to_object(self, data : dict) -> Edible:
        return Edible(data["name"], data["type"], data["calories"])
    
    def get_persistence(self):
        return EdibleDAO.get_instance()

        