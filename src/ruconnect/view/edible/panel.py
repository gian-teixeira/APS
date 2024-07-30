from view.edible.search import EdibleSearch
from view.edible.register import EdibleRegister
from model.session import Session
from model.user import Administrator

import tkinter as tk
from tkinter import ttk, font as tk_font
        
class EdiblePanel(tk.Frame):
    def __init__(self):
        super().__init__()
        
        self.title = ttk.Label(self, text = "Comida", font = tk_font.BOLD)
        self.sep = ttk.Separator(self, orient = tk.HORIZONTAL)
        self.tab_controller = ttk.Notebook(self)

        tabs = dict()

        tabs["Busca"] = ttk.Frame(self.tab_controller)
        self.tab_controller.add(tabs["Busca"], text = "Busca")
        self.search_frame = ttk.Frame(tabs["Busca"])
        search = EdibleSearch()
        search.pack(in_ = self.search_frame, expand = True, anchor = 'n')
        self.search_frame.pack(expand = True, fill = tk.BOTH)
        
        if isinstance(Session.get_user(), Administrator):
            tabs["Registro"] = ttk.Frame(self.tab_controller)
            self.tab_controller.add(tabs["Registro"], text = "Registro")
            self.register_frame = ttk.Frame(tabs["Registro"])
            register = EdibleRegister()
            register.pack(in_ = self.register_frame, expand = True, anchor = 'n')
            self.register_frame.pack(expand = True, fill = tk.BOTH)

        self.title.pack(fill = tk.BOTH)
        self.sep.pack(fill = tk.X)
        self.tab_controller.pack(expand = True, fill = tk.BOTH)