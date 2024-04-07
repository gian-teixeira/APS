from persistence.daily_menu import DailyMenuPersistence
from control.daily_menu import DailyMenuController
from model.daily_menu import DailyMenu
from view.entry import Entry

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

        self.__frame = ttk.Frame(self)
        self.__entry = Entry("Data")
        self.__confirm_button = ttk.Button(self.__frame, text = "Registrar", command = self.confirm)

        self.__frame.pack(expand = True, padx = 10, pady = 10)
        self.__entry.pack(in_ = self.__frame)
        self.__confirm_button.pack(pady = 10)

    def confirm(self):
        edible_name = self.__entry.get_content()
        edible = DailyMenu()

        self.__error_label.pack_forget()
        try:
            self.__search_result = self.__controller.save(edible)
        except:
            self.__error_label.pack(expand = True)
        else:
            self.__entry.clear()