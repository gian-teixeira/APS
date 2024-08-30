from persistence.dao.DAO import DAO

class EdibleDAO(DAO):
    @property
    def filename(self) -> str:
        return "edible"