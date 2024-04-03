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