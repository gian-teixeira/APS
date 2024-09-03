from persistence import Serializable

class StudentConsumption(Serializable):
    def __init__(self, student_id : int, spent_credits : int, days_attended : list[str]):
        self.student_id = student_id
        self.spent_credits = spent_credits
        self.days_attended = days_attended

    @property
    def id(self) -> str:
        return self.student_id
