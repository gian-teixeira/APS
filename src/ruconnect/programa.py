from persistence.persistence import Persistence
from view.login.panel import LoginPanel
from view.view import View

class Programa:
    user = None
    display = None

    @classmethod
    def set_user(cls, user):
        cls.user = user
        cls.display.destroy()
        cls.display = View(user)
        cls.display.mainloop()

    @classmethod
    def main(cls):
        Persistence.set_database_folder("./data")
        cls.display = LoginPanel(cls.set_user)
        cls.display.mainloop()

if __name__ == "__main__":
    Programa.main()