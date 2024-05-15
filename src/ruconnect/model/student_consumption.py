class StudentConsumption:
    def __init__(self, student_id : int, spent_credits : int, days_attended : int):
        self.student_id = student_id
        self.spent_credits = spent_credits
        self.days_attended = days_attended

    def get_student_id(self) -> int:
        return self.student_id
    
    def set_student_id(self, student_id : int) -> None:
        self.student_id = student_id
    
    def get_spent_credits(self) -> str:
        return self.spent_credits
    
    def set_spent_credits(self, spent_credits: str) -> None:
        self.spent_credits = spent_credits
    
    def get_days_attended(self) -> str:
        return self.days_attended
    
    def set_days_attended(self, days_attended : str) -> None:
        self.days_attended = days_attended
        
    def to_dict(self) -> dict:
        return {
            "student_id" : self.get_student_id(),
            "spent_credits" : self.get_spent_credits(),
            "days_attended" : self.get_days_attended()
        }
