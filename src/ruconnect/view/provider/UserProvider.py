from view.provider.Provider import Provider
from model.User import Administrator, Student

class StudentProvider(Provider):
    @staticmethod
    def label(obj: Student) -> str:
        return obj.id
    
    @staticmethod
    def info(obj: Student) -> tuple[tuple[str,str]]:
        return (
            ('Nome', obj.name),
            ('CPF', obj.calories),
            ('Senha', obj.password),
            ('Creditos', obj.credit)
        )

class AdministratorProvider(Provider):
    @staticmethod
    def label(obj: Administrator) -> str:
        return obj.id

    @staticmethod
    def info(obj: Administrator) -> tuple[tuple[str,str]]:
        return (
            ('Nome', obj.name),
            ('CPF', obj.calories),
            ('Senha', obj.password)
        )