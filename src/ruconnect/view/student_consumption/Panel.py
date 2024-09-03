from view.student_consumption.Search import StudentConsumptionSearch
from view.student_consumption.Register import StudentConsumptionRegister
from view.Session import Session
from model.User import User

import tkinter as tk
from tkinter import ttk, font as tk_font
        
class StudentConsumptionPanel(tk.Frame):
    def __init__(self):
        super().__init__()
        
        self.title = ttk.Label(self, text = "Registro de Consumo", font = tk_font.BOLD)
        self.sep = ttk.Separator(self, orient = tk.HORIZONTAL)
        self.tab_controller = ttk.Notebook(self)

        tabs = dict()

        tabs["Busca"] = ttk.Frame(self.tab_controller)
        self.tab_controller.add(tabs["Busca"], text = "Busca")
        self.search_frame = ttk.Frame(tabs["Busca"])
        search = StudentConsumptionSearch()
        search.pack(in_ = self.search_frame, expand = True, anchor = 'n')
        self.search_frame.pack(expand = True, fill = tk.BOTH)
        
        if isinstance(Session.get_user(), User):
            tabs["Registro"] = ttk.Frame(self.tab_controller)
            self.tab_controller.add(tabs["Registro"], text = "Registro")
            self.register_frame = ttk.Frame(tabs["Registro"])
            register = StudentConsumptionRegister()
            register.pack(in_ = self.register_frame, expand = True, anchor = 'n')
            self.register_frame.pack(expand = True, fill = tk.BOTH)

        self.title.pack(fill = tk.BOTH)
        self.sep.pack(fill = tk.X)
        self.tab_controller.pack(expand = True, fill = tk.BOTH)