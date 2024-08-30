class Feedback:
    def __init__(self, star_rating : int, written_rating : str, date_menu : str, period_menu : str, id_rater : str):
        self.star_rating = star_rating
        self.written_rating = written_rating
        self.id_menu = f'{date_menu} - {period_menu}'
        self.id_rater = id_rater

    def get_id(self) -> str:
        return self.id_rater + self.id_menu