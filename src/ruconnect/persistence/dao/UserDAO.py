from persistence.dao.DAO import DAO

class StudentDAO(DAO):
    @property
    def filename(self) -> str:
        return "student"

class AdministratorDAO(DAO):
    @property
    def filename(self) -> str:
        return "administrator"