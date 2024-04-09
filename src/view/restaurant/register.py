from persistence.restaurant import RestaurantPersistence
from control.restaurant import RestaurantController
from model.restaurant import Restaurant
from view.entry import Entry
from view.selector import Selector

import tkinter as tk
from tkinter import ttk

class RestaurantRegister(ttk.Frame):
    def __init__(self):
        super().__init__()

        self.__persistence = RestaurantPersistence()
        self.__controller = RestaurantController(self.__persistence)

        #self.__error_label = ttk.Label(self, 
        #                               text = "Item já cadastrado",
         #                              foreground = "red",
        #                               relief = tk.GROOVE,
         #                              justify = 'center')

        self.__frame = ttk.Frame(self)
        self.__name_entry = Entry("Restaurante")
        self.__operating_time_entry = Entry("Tempo de funcionamento")
        self.__price = Entry("Preço")
    
        self.__confirm_button = ttk.Button(self.__frame, text = "Registrar", command = self.confirm)

        self.__frame.pack(expand = True, padx = 10, pady = 10)
        self.__name_entry.pack(in_ = self.__frame)
        self.__operating_time.pack(in_ = self.__frame)
        self.__price.pack(in_ = self.__frame)
        self.__confirm_button.pack(pady = 10)

    def confirm(self):
        restaurant = Restaurant()
        restaurant.set_name(self.__name_entry.get_content())
        restaurant.set_operating_time(self.__operating_time.get_content())
        restaurant.set_price(float(self.__price.get_content()))

        #self.__error_label.pack_forget()
        try:
            self.__search_result = self.__controller.save(restaurant)
        except Exception as e:
            self.__error_label.pack(expand = True)
        else:
            self.__name_entry.clear()
            self.__operating_time_entry.clear()
            self.__price.clear()