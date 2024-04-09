from persistence.daily_menu import DailyMenuPersistence
from persistence.edible import EdiblePersistence
from control.daily_menu import DailyMenuController
from control.edible import EdibleController
from model.daily_menu import DailyMenu
from view.entry import Entry
from view.selector import Selector
from persistence.daily_menu import DailyMenuPersistence
from control.daily_menu import DailyMenuController

import tkinter as tk
from tkinter import ttk

class DailyMenuRegister(ttk.Frame):
    def __init__(self):
        super().__init__()

        self.__persistence = DailyMenuPersistence()
        self.__controller = DailyMenuController(self.__persistence)
        self.__error_label = ttk.Label(self, 
                                       text = "Item já cadastrado",
                                       foreground = "red",
                                       relief = tk.GROOVE,
                                       justify = 'center')
        self.__right = ttk.Frame(self)
        self.__left = ttk.Frame(self)
        self.__data_entry = Entry("Data")
        self.__confirm_button = ttk.Button(self.__right, 
                                           text = "Registrar", 
                                           command = self.confirm)
        self.__edible_search_button = ttk.Button(self.__left, text = "Atualizar alimentos", command = self.update)
        self.__period_selector = Selector("Período", ["Almoço", "Jantar"])
        self.__listbox = tk.Listbox(self.__left, selectmode="multiple", highlightthickness = 0)
        self.__listbox_scroll = tk.Scrollbar(self.__left)

        self.__listbox.config(yscrollcommand = self.__listbox_scroll.set)
        self.__listbox_scroll.config(command = self.__listbox.yview)

        self.__left.pack(expand = True, side = tk.LEFT, padx = 10, pady = 10)
        self.__right.pack(expand = True, side = tk.RIGHT, padx = 10, pady = 10)
        self.__data_entry.pack(in_ = self.__right, expand = True)
        self.__period_selector.pack(in_ = self.__right)
        self.__confirm_button.pack(pady = 10)
        self.__listbox.pack(expand = True)
        self.__edible_search_button.pack(pady = 10)

        self.__persistence = DailyMenuPersistence()
        self.__controller = DailyMenuController(self.__persistence)

    def confirm(self):
        edible_persistence = EdiblePersistence()
        edible_controller = EdibleController(edible_persistence)
        menu_persistence = DailyMenuPersistence()
        menu_controller = DailyMenuController(menu_persistence)

        date = self.__data_entry.get_content()
        registered = menu_controller.search_by_date(date)
        replace = len(registered) != 0

        menu = DailyMenu(date)
        selected_edibles = [edible_controller.search()[index]
                            for index in self.__listbox.curselection()]
        
        match self.__period_selector.get_selection():
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

        self.__data_entry.clear()
        self.__period_selector.clear()


    def update(self):
        edible_persistence = EdiblePersistence()
        edible_controller = EdibleController(edible_persistence)

        for edible in edible_controller.search():
            if edible is None: continue
            self.__listbox.insert(tk.END, edible.get_name())
