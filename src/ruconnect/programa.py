from persistence.Persistence import Persistence
from view.login.Panel import LoginPanel
from view.View import View
from view.Session import Session
from sys import argv

class Programa:
    user = None
    display = None

    @classmethod
    def login(cls, user):
        Session.set_user(user)
        cls.display.destroy()
        cls.display = View()
        cls.display.mainloop()

    @classmethod
    def main(cls):
        Persistence.set_database_folder("./data")
        cls.display = LoginPanel(cls.login)
        if len(argv) > 1:
            cls.display.enter(force = True)
        cls.display.mainloop()

if __name__ == "__main__":
    Programa.main()