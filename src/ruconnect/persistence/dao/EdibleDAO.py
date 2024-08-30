from persistence import DAO

class EdibleDAO(DAO):
    @property
    def filename(self) -> str:
        return "edible"