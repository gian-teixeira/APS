import datetime

class Restaurant:
    _instance = None

    @classmethod
    def get_instance(cls):
        if cls._instance is None: 
            cls._instance = Restaurant()
        return cls._instance

    

print(Restaurant.credit_price)
Restaurant.credit_price = 10
