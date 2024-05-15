from control.controller import Controller
from model.student_consumption import StudentConsumption

class StudentConsumptionController(Controller):
    def __init__(self, persistence):
        super().__init__(persistence, StudentConsumption)

    def search(self, student_id):
        return super().search(None if student_id is None else {
            "student_id" : student_id
        })
    
    def delete(self, student_id):
        super().delete({
            "student_id" : student_id
        })
    
    def build_object(self, data):
        return StudentConsumption(*data.values())