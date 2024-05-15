from persistence.persistence import Persistence

class FeedbackPersistence(Persistence):
    def __init__(self):
        super().__init__("feedback")