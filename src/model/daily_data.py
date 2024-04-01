class DailyData:
    def __init__(self):
        _sold_credits = 0
        _access_count = 0

    @property
    def sold_credits(self):
        return self._sold_credits
    
    @property
    def access_count(self):
        return self._access_count
    
    def increase_sold_credits(self,value : int):
        self._sold_credits += value

    def increase_access_count(self,value : int):
        self._access_count += value

    