from persistence import Serializable

class Feedback(Serializable):
    def __init__(self,
                 star_rating : int, 
                 written_rating : str, 
                 menu_date : str, 
                 menu_period : str,
                 rater_id : str):
        self.star_rating = star_rating
        self.written_rating = written_rating
        self.menu_date = menu_date
        self.menu_period = menu_period
        self.rater_id = rater_id

    @property
    def id(self) -> str:
        return f"{self.rater_id} {self.menu_date} {self.menu_period}"