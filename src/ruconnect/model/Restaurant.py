from persistence import Serializable

class Restaurant(Serializable):
    instance = None
    price : float = 0
    name : str = ""
    operating_time : tuple[str,str] = ("", "")

    @property
    def id(self) -> str:
        return 0
    
    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = cls()
        return cls.instance