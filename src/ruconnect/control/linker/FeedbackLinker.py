from control.linker.Linker import Linker
from model import Feedback
from persistence import FeedbackDAO

class FeedbackLinker(Linker):
    def to_dict(self, obj : Feedback) -> dict:
        return {
            "star_rating" : obj.star_rating,
            "written_rating" : obj.written_rating,
            "menu_date" : obj.menu_date,
            "menu_period" : obj.menu_period,
            "id_rater" : obj.rater_id,
        }

    def to_object(self, data : dict) -> Feedback:
        return Feedback(data["star_rating"], 
            data["written_rating"], data["menu_date"],
            data["menu_period"], data["id_rater"])
    
    def get_persistence(self):
        return FeedbackDAO.get_instance()