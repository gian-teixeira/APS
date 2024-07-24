class Feedback:
    def __init__(self, star_rating : int, written_rating : str, date_menu : str, period_menu : str, id_student : str):
        self.star_rating = star_rating
        self.written_rating = written_rating
        self.id = f'{date_menu} - {period_menu}'
        self.id_student = id_student

    def get_star_rating(self) -> int:
        return self.star_rating
    
    def set_star_rating(self, star_rating : int) -> None:
        self.star_rating = star_rating
    
    def get_written_rating(self) -> str:
        return self.written_rating
    
    def set_written_rating(self, written_rating: str) -> None:
        self.written_rating = written_rating
    
    def get_id(self) -> str:
        return self.id
    
    def set_id(self, id : str) -> None:
        self.id = id
        
    def to_dict(self) -> dict:
        return {
            "star_rating" : self.get_star_rating(),
            "written_rating" : self.get_written_rating(),
            "id" : self.get_id(),
        }
