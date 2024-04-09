from persistence.persistence import Persistence
from persistence.edible import EdiblePersistence
from control.edible import EdibleController
from view.edible.panel import EdiblePanel
from view.view import View
from sys import argv

import tkinter as tk
from view.panel import Panel

if __name__ == "__main__":
    database_folder = argv[1]
    print(database_folder)
    Persistence.set_database_folder(database_folder)

    root = View()
    persistence = EdiblePersistence()
    controller = EdibleController(persistence)

    print(controller.delete_by_name)

    root.mainloop()
