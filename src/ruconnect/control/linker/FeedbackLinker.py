from control.linker.Linker import Linker
from model import Feedback
from persistence import FeedbackDAO

class FeedbackLinker(Linker):
    def to_dict(self, obj : Feedback) -> dict:
        return {
            "star_rating" : obj.star_rating,
            "written_rating" : obj.written_rating,
            "id_menu" : obj.id_menu,
            "id_rater" : obj.cpf,
        }

    def to_object(self, data : dict) -> Feedback:
        return Feedback(data["star_rating"], data["written_rating"], data["id_menu"], data["id_rater"])
    
    def get_persistence(self):
        return FeedbackDAO.get_instance()