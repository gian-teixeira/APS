from control.linker.Linker import Linker
from model import Administrator
from persistence import AdministratorDAO

class AdministratorLinker(Linker):
    def to_dict(self, obj : Administrator) -> dict:
        return {
            "name": obj.name,
            "cpf": obj.cpf, 
            "password": obj.password,
        }
        
    def to_object(self, data : dict) -> Administrator:
        print("to_object : ", data)
        return Administrator(data["name"], data["cpf"], data["password"])
    
    def get_persistence(self):
        return AdministratorDAO.get_instance()