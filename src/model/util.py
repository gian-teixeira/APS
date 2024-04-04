from datetime import date

class TypeException(TypeError):
    def __init__(self,
                 expected : type,
                 got : type):
        super().__init__(f"must be {expected} not {got}")
    
    @staticmethod
    def check_type(obj : object,
                   expected : type):
        if not isinstance(obj, expected):
            raise TypeException(expected, type(obj))
        
class DateTime:
    @staticmethod
    def date_format() -> str:
        return "%Y:%M:%H"
    
    @staticmethod
    def date_string(date : date) -> str:
        return date.strftime(DateTime.date_format())