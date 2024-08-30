from control.controller.DailyMenuController import DailyMenuController
from control.controller.EdibleController import EdibleController
from control.controller.DailyMenuController import DailyMenuController

from model.DailyMenu import DailyMenu
from view.Entry import Entry
from view.Selector import Selector
from view.SearchBox import SearchBox

import tkinter as tk
from tkinter import ttk

class DailyMenuRegister(ttk.Frame):
    def __init__(self):
        super().__init__()
        self.error_label = ttk.Label(self, 
                                       text = "Item já cadastrado",
                                       foreground = "red",
                                       relief = tk.GROOVE,
                                       justify = 'center')
        self.right = ttk.Frame(self)
        self.left = ttk.Frame(self)
        self.data_entry = Entry("Data")
        self.period_selector = Selector("Período", ["Almoço", "Jantar"])
        self.search = SearchBox(EdibleController(), ["Alimentos"], tk.MULTIPLE)

    def confirm(self):
        edible_controller = EdibleController()
        menu_controller = DailyMenuController()

        date = self.data_entry.get_content()
        menu = menu_controller.read(date)

        if menu is None:
            menu = DailyMenu(date)
            menu_controller.create(menu)

        selected_edibles = [
            edible_controller.read()[index]
            for index in self.listbox.curselection()]

        match self.period_selector.get_selection():
            case "Almoço":
                menu.lunch_erase()
                for edible in selected_edibles:
                    menu.lunch_add([edible])
            case "Jantar": 
                menu.dinner_erase()
                for edible in selected_edibles:
                    menu.dinner_add([edible])
        
        menu_controller.update(menu)
        self.data_entry.clear()
        self.period_selector.clear()


    def update(self):
        edible_controller = EdibleController()

        for edible in edible_controller.read():
            if edible is None: continue
            self.listbox.insert(tk.END, edible.get_name())

    def pack(self, *args, **kwargs):
        self.left.pack(expand = True, side = tk.LEFT, padx = 10, pady = 10)
        self.right.pack(expand = True, side = tk.RIGHT, padx = 10, pady = 10)
        self.data_entry.pack(in_ = self.right, expand = True)
        self.period_selector.pack(in_ = self.right)
        self.search.pack(in_ = self.left)
        super().pack(*args, **kwargs)
