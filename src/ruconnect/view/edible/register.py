from persistence.edible import EdiblePersistence
from control.edible import EdibleController
from model.edible import Edible
from model.edible_type import EdibleType
from view.entry import Entry
from view.selector import Selector

import tkinter as tk
from tkinter import ttk

class EdibleRegister(ttk.Frame):
    def __init__(self):
        super().__init__()

        self.__persistence = EdiblePersistence()
        self.__controller = EdibleController(self.__persistence)

        self.__error_label = ttk.Label(self, 
                                       text = "Item já cadastrado",
                                       foreground = "red",
                                       relief = tk.GROOVE,
                                       justify = 'center')
        
        self.__frame = ttk.Frame(self)
        self.__name_entry = Entry("Nome")
        self.__calories_entry = Entry("Calorias")
        self.__type_selector = Selector("Tipo", [t.value for t in EdibleType])
        self.__confirm_button = ttk.Button(self.__frame, text = "Registrar", command = self.confirm)

        self.__frame.pack(expand = True, padx = 10, pady = 10)
        self.__name_entry.pack(in_ = self.__frame)
        self.__calories_entry.pack(in_ = self.__frame)
        self.__type_selector.pack(in_ = self.__frame)
        self.__confirm_button.pack(pady = 10)

    def confirm(self):
        edible = Edible(self.__name_entry.get_content(),
                        self.__type_selector.get_selection(),
                        int(self.__calories_entry.get_content()))

        self.__error_label.pack_forget()
        try:
            self.__search_result = self.__controller.save(edible)
        except Exception as e:
            self.__error_label.pack(expand = True)
        else:
            self.__name_entry.clear()
            self.__calories_entry.clear()
            self.__type_selector.clear()
        