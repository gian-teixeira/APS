from persistence.persistence import Persistence
from sys import argv

import tkinter as tk
from view.pane import Panel

if __name__ == "__main__":
    database_folder = argv[1]
    print(database_folder)
    Persistence.set_database_folder(database_folder)

    root = tk.Tk()
    panel = Panel("Cardápio")
    panel.pack(in_ = root, expand = True, fill = tk.BOTH)

    root.mainloop()
