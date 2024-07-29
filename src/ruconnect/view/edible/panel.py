from view.edible.search import EdibleSearch
from view.edible.register import EdibleRegister

import tkinter as tk
from tkinter import ttk, font as tk_font
        
class EdiblePanel(tk.Frame):
    def __init__(self):
        super().__init__()
        
        title = ttk.Label(self, text = "Comida", font = tk_font.BOLD)
        sep = ttk.Separator(self, orient = tk.HORIZONTAL)
        tab_controller = ttk.Notebook(self)

        tab_names = ["Busca", "Registro"]
        tabs = dict()

        for tab_name in tab_names:
            tabs[tab_name] = ttk.Frame(tab_controller)
            tab_controller.add(tabs[tab_name], text = tab_name)

        search_frame = ttk.Frame(tabs["Busca"])
        search = EdibleSearch()
        search.pack(in_ = search_frame, expand = True, anchor = 'n')
        search_frame.pack(expand = True, fill = tk.BOTH)
        
        register_frame = ttk.Frame(tabs["Registro"])
        register = EdibleRegister()
        register.pack(in_ = register_frame, expand = True, anchor = 'n')
        register_frame.pack(expand = True, fill = tk.BOTH)

        title.pack(fill = tk.BOTH)
        sep.pack(fill = tk.X)
        tab_controller.pack(expand = True, fill = tk.BOTH)