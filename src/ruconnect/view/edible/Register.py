from control.controller.EdibleController import EdibleController
from model.Edible import Edible
from model.EdibleType import EdibleType
from view.Entry import Entry
from view.Selector import Selector

import tkinter as tk
from tkinter import ttk

class EdibleRegister(ttk.Frame):
    def __init__(self):
        super().__init__()

        self.controller = EdibleController()
        self.error_label = ttk.Label(self, text = "Item já cadastrado", foreground = "red", 
                                     relief = tk.GROOVE, justify = 'center')
        
        self.frame = ttk.Frame(self)
        self.name_entry = Entry("Nome")
        self.calories_entry = Entry("Calorias")
        self.type_selector = Selector("Tipo", [t.value for t in EdibleType])
        self.confirm_button = ttk.Button(self.frame, text = "Registrar", command = self.confirm)
        
        self.frame.pack(expand = True, padx = 10, pady = 10)
        self.name_entry.pack(in_ = self.frame)
        self.calories_entry.pack(in_ = self.frame)
        self.type_selector.pack(in_ = self.frame)
        self.confirm_button.pack(pady = 10)

    def confirm(self):
        edible = Edible(self.name_entry.get_content(),
                        self.type_selector.get_selection(),
                        int(self.calories_entry.get_content()))

        self.error_label.pack_forget()
        try:
            self.controller.create(edible)
        except Exception as e:
            self.error_label.pack(expand = True)
        else:
            self.name_entry.clear()
            self.calories_entry.clear()
            self.type_selector.clear()
        