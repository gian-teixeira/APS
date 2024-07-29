from persistence.meal_register import MealRegisterPersistence
from control.meal_register import MealRegisterController
from persistence.daily_menu import DailyMenuPersistence
from control.daily_menu import DailyMenuController
from persistence.user import StudentPersistence
from control.user import StudentController
from model.meal_register import MealRegister
from view.entry import Entry
from view.selector import Selector
from view.search_box import SearchBox

import tkinter as tk
from tkinter import ttk

class MealRegisterRegister(ttk.Frame):
    def __init__(self):
        super().__init__()

        self.persistence = MealRegisterPersistence()
        self.controller = MealRegisterController(self.persistence)
        self.error_label = ttk.Label(self, text = "Item já cadastrado", foreground = "red", 
                                     relief = tk.GROOVE, justify = 'center')
        
        self.frame = ttk.Frame(self)
        self.name_search = SearchBox(StudentController(StudentPersistence()), "Aluno")
        self.menu_search = SearchBox(DailyMenuController(DailyMenuPersistence()), "Menu")
        self.confirm_button = ttk.Button(self.frame, text = "Registrar", command = self.confirm) 

    def confirm(self):
        edible = MealRegister(self.name_search.curselection(), 
                              self.menu_search.curselection())

        self.error_label.pack_forget()
        try:
            self.search_result = self.controller.save(edible)
        except Exception as e:
            self.error_label.pack(expand = True)
        else:
            self.name_entry.clear()
            self.date_entry.clear()

    def pack(self, *args, **kwargs):
        self.name_search.pack(in_ = self.frame, side = tk.RIGHT, padx = 10, pady = 50)
        self.menu_search.pack(in_ = self.frame, side = tk.LEFT, padx = 10, pady = 50)
        self.frame.pack()
        self.confirm_button.pack(side = tk.BOTTOM)
        super().pack(*args, **kwargs)
        