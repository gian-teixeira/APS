from control.linker.Linker import Linker
from model import StudentConsumption
from persistence import StudentConsumptionDAO

class RestaurantLinker(Linker):
    def to_dict(self, obj : StudentConsumption) -> dict:
        return {
            "student_id" : obj.student_id,
            "spent_credits" : obj.spent_credits,
            "days_attended" : obj.days_attended,
        }        

    def to_object(self, data : dict) -> StudentConsumption:
        return StudentConsumption(data["student_id"], data["spent_credits"], data["days_attended"])
    
    def get_persistence(self):
        return StudentConsumptionDAO.get_instance()