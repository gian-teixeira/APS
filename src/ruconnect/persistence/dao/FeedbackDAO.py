from persistence.dao.DAO import DAO

class FeedbackDAO(DAO):
    @property
    def filename(self) -> str:
        return "feedback"