from view.feedback.search import FeedbackSearch
from view.user.register import UserRegister
from model.user import Administrator

import tkinter as tk
from tkinter import ttk, font as tk_font
        
class UserPanel(tk.Frame):
    def __init__(self):
        super().__init__()
        
        title = ttk.Label(self, text = "Avaliação", font = tk_font.BOLD)
        sep = ttk.Separator(self, orient = tk.HORIZONTAL)
        tab_controller = ttk.Notebook(self)

        tab_names = ["Busca", "Registro"]
        tabs = dict()

        for tab_name in tab_names:
            tabs[tab_name] = tk.Frame(tab_controller)
            tab_controller.add(tabs[tab_name], text = tab_name)
        
        register_frame = tk.Frame(tabs["Registro"])
        register = UserRegister()
        register.pack(in_ = register_frame, expand = True, anchor = 'n')
        register_frame.pack(expand = True, fill = tk.BOTH)

        title.pack(fill = tk.BOTH)
        sep.pack(fill = tk.X)
        tab_controller.pack(expand = True, fill = tk.BOTH)