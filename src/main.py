from persistence.persistence import Persistence
from sys import argv

if __name__ == "__main__":
    database_folder = argv[1]
    print(database_folder)
    Persistence.set_database_folder(database_folder)