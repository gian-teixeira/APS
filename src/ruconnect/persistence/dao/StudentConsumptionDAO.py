from persistence.dao.DAO import DAO

class StudentConsumptionDAO(DAO):
    @property
    def filename(self) -> str:
        return "student_consumption"