from view.provider.Provider import Provider
from model import Feedback

class FeedbackProvider(Provider):
    @staticmethod
    def label(obj: Feedback) -> str:
        return obj.id

    @staticmethod
    def info(obj: Feedback) -> tuple[tuple[str,str]]:
        return (
            ("Estrelas",  obj.star_rating),
            ("Comentário",  obj.written_rating),
            ("ID do Menu",  obj.id_menu),
            ("CPF",  obj.cpf)
        )