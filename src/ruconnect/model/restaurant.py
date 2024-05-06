class Restaurant:
    instance = None
    price : float = 0
    name : str = ""
    operating_time : tuple[str,str] = ("", "")
    
    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = cls()
        return cls.instance
    
    def get_price(self) -> float:
        return self.price
    
    def get_name(self) -> str:
        return self.name
    
    def get_operating_time(self) -> tuple[str,str]:
        return self.operating_time
    
    def set_price(self, price) -> None:
        self.price = price

    def set_name(self, name) -> None:
        self.name = name
    
    def set_operating_time(self, operating_time : tuple[str,str]):
        self.operating_time = operating_time

    def to_dict(self) -> dict:
        return {
            "name" : self.get_name(),
            "time" : self.get_operating_time(),
            "price" : self.get_price()
        }
    
    def attr_labels(self) -> tuple:
        return ("Nome", "Tempo de Funcionamento", "Preço")