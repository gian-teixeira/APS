from persistence.persistence import Persistence
from view.view import View
from sys import argv

if __name__ == "__main__":
    database_folder = argv[1]
    
    Persistence.set_database_folder(database_folder)

    root = View()
    root.mainloop()
