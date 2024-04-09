from persistence.persistence import Persistence
from view.view import View
from sys import argv

class Programa:
    @staticmethod
    def main():
        Persistence.set_database_folder("./data")
        root = View()
        root.mainloop()

if __name__ == "__main__":
    Programa.main()