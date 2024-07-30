from view.daily_menu.search import DailyMenuSearch
from view.daily_menu.register import DailyMenuRegister
from model.session import Session
from model.user import Administrator

import tkinter as tk
from tkinter import ttk, font as tk_font
        
class DailyMenuPanel(tk.Frame):
    def __init__(self):
        super().__init__()
        
        title = ttk.Label(self, text = "Cardápio", font = tk_font.BOLD)
        sep = ttk.Separator(self, orient = tk.HORIZONTAL)
        tab_controller = ttk.Notebook(self)

        tabs = dict()

        tabs["Busca"] = ttk.Frame(tab_controller)
        tab_controller.add(tabs["Busca"], text = "Busca")
        search_frame = ttk.Frame(tabs["Busca"])
        search = DailyMenuSearch()
        search.pack(in_ = search_frame, expand = True, anchor = 'n')
        search_frame.pack(expand = True, fill = tk.BOTH)
        
        if isinstance(Session.get_user(), Administrator):
            tabs["Registro"] = ttk.Frame(tab_controller)
            tab_controller.add(tabs["Registro"], text = "Registro")
            register_frame = tk.Frame(tabs["Registro"])
            register = DailyMenuRegister()
            register.pack(in_ = register_frame, expand = True, anchor = 'n')
            register_frame.pack(expand = True, fill = tk.BOTH)

        title.pack(fill = tk.BOTH)
        sep.pack(fill = tk.X)
        tab_controller.pack(expand = True, fill = tk.BOTH)