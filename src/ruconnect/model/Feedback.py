from persistence import Serializable

class Feedback(Serializable):
    def __init__(self,
                 star_rating : int, 
                 written_rating : str, 
                 menu_date : str, 
                 menu_period : str,
                 id_rater : str):
        self.star_rating = star_rating
        self.written_rating = written_rating
        self.menu_date = menu_date
        self.menu_period = menu_period
        self.id_rater = id_rater

    @property
    def id(self) -> str:
        return f"{self.id_rater} {self.menu_date} {self.menu_period}"