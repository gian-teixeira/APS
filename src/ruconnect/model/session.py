class Session:
    user = None

    @classmethod
    def set_user(cls, user):
        cls.user = user
    
    @classmethod
    def get_user(cls):
        return cls.user