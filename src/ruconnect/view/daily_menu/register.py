from persistence.daily_menu import DailyMenuPersistence
from persistence.edible import EdiblePersistence
from control.daily_menu import DailyMenuController
from control.edible import EdibleController
from model.daily_menu import DailyMenu
from view.entry import Entry
from view.selector import Selector
from persistence.daily_menu import DailyMenuPersistence
from control.daily_menu import DailyMenuController
from view.search_box import SearchBox

import tkinter as tk
from tkinter import ttk

class DailyMenuRegister(ttk.Frame):
    def __init__(self):
        super().__init__()

        self.persistence = DailyMenuPersistence()
        self.controller = DailyMenuController(self.persistence)
        self.error_label = ttk.Label(self, 
                                       text = "Item já cadastrado",
                                       foreground = "red",
                                       relief = tk.GROOVE,
                                       justify = 'center')
        self.right = ttk.Frame(self)
        self.left = ttk.Frame(self)
        self.data_entry = Entry("Data")
        self.period_selector = Selector("Período", ["Almoço", "Jantar"])
        self.search = SearchBox(EdibleController(EdiblePersistence()), "Alimentos", tk.MULTIPLE)


        self.persistence = DailyMenuPersistence()
        self.controller = DailyMenuController(self.persistence)

    def confirm(self):
        edible_persistence = EdiblePersistence()
        edible_controller = EdibleController(edible_persistence)
        menu_persistence = DailyMenuPersistence()
        menu_controller = DailyMenuController(menu_persistence)

        date = self.data_entry.get_content()
        registered = menu_controller.search_by_date(date)
        replace = len(registered) != 0

        menu = DailyMenu(date)
        selected_edibles = [edible_controller.search_helper()[index]
                            for index in self.listbox.curselection()]
        
        match self.period_selector.get_selection():
            case "Almoço":
                if replace: menu.dinner_add(registered[0].get_dinner())
                for edible in selected_edibles:
                    menu.lunch_add([edible])
            case "Jantar": 
                if replace: menu.lunch_add(registered[0].get_lunch())
                for edible in selected_edibles:
                    menu.dinner_add([edible])

        if replace:
            menu_controller.delete_by_date(date)
        menu_controller.save(menu)

        self.data_entry.clear()
        self.period_selector.clear()


    def update(self):
        edible_persistence = EdiblePersistence()
        edible_controller = EdibleController(edible_persistence)

        for edible in edible_controller.search():
            if edible is None: continue
            self.listbox.insert(tk.END, edible.get_name())

    def pack(self, *args, **kwargs):
        self.left.pack(expand = True, side = tk.LEFT, padx = 10, pady = 10)
        self.right.pack(expand = True, side = tk.RIGHT, padx = 10, pady = 10)
        self.data_entry.pack(in_ = self.right, expand = True)
        self.period_selector.pack(in_ = self.right)
        self.search.pack(in_ = self.left)
        super().pack(*args, **kwargs)
