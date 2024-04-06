from view.search import SearchPanel
from control.controller import Controller
import tkinter as tk
from tkinter import ttk, font as tk_font

class Panel(tk.Frame):
    def __init__(self,
                 name : str,
                 controller : Controller,
                 search_callback):
        super().__init__()
        self.__name = name
        self.__controller = controller
        self.__search_callback = search_callback
        
        title = ttk.Label(self, text = self.__name, font = tk_font.BOLD)
        sep = ttk.Separator(self, orient = tk.HORIZONTAL)
        tab_controller = ttk.Notebook(self)

        tab_names = ["Busca", "Registro"]
        tabs = dict()

        for tab_name in tab_names:
            tabs[tab_name] = tk.Frame(tab_controller)
            tab_controller.add(tabs[tab_name], text = tab_name)

        for tab_name in tab_names:
            frame = tk.Frame(tabs[tab_name])
            search = SearchPanel(self.__controller.search_requests(),
                                 self.__search_callback)
            search.pack(in_ = frame)
            frame.pack(expand = True, fill = tk.BOTH)

        title.pack(fill = tk.BOTH)
        sep.pack(fill = tk.X)
        tab_controller.pack(expand = True, fill = tk.BOTH)


