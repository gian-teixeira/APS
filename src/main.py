from persistence.persistence import Persistence
from persistence.edible import EdiblePersistence
from control.edible import EdibleController
from sys import argv

import tkinter as tk
from view.panel import Panel

if __name__ == "__main__":
    database_folder = argv[1]
    print(database_folder)
    Persistence.set_database_folder(database_folder)

    root = tk.Tk()
    persistence = EdiblePersistence()
    controller = EdibleController(persistence)

    #persistence.register({ "name" : "arroz" })
    #persistence.register({ "name" : "feijão" })

    panel = Panel("Comida", controller, controller.search_by_name)
    panel.pack(in_ = root, expand = True, fill = tk.BOTH,
               padx = 10, pady = 10)

    root.mainloop()
