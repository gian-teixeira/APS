class StudentConsumption:
    def __init__(self, student_id : int, spent_credits : int, days_attended : int):
        self.student_id = student_id
        self.spent_credits = spent_credits
        self.days_attended = days_attended

    def get_id(self) -> str:
        return self.student_id
