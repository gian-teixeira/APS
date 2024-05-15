from control.controller import Controller
from model.feedback import Feedback

class FeedbackController(Controller):
    def __init__(self, persistence):
        super().__init__(persistence, Feedback)

    def search(self, id):
        return super().search(None if id is None else {
            "id" : id
        })
  
    def delete(self, id):
        super().delete({
            "id" : id
        })
    
    def build_object(self, data):
        return Feedback(*data.values())