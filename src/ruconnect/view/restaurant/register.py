from persistence.restaurant import RestaurantPersistence
from control.restaurant import RestaurantController
from model.restaurant import Restaurant
from view.entry import Entry
from view.card import Card

import tkinter as tk
from tkinter import ttk

class RestaurantRegister(tk.Frame):
    def __init__(self):
        super().__init__()

        self.__persistence = RestaurantPersistence()
        self.__controller = RestaurantController(self.__persistence)
        self.__name_entry = Entry("Restaurante")
        self.__price = Entry("Preço")
        self.__left = tk.Frame(self)
        self.__right = tk.Frame(self)
        self.__time_frame = tk.Frame(self.__left)
        self.__lunch_time_entry = Entry("Horário Almoço")
        self.__dinner_time_entry = Entry("Horário Jantar")
        self.__card = None

        self.__confirm_button = ttk.Button(self.__left, text = "Registrar", command = self.confirm)

        self.__left.pack(expand = True, side= tk.TOP)
        self.__right.pack(expand = True, side= tk.BOTTOM)
        self.__name_entry.pack(in_ = self.__left)
        self.__lunch_time_entry.pack(in_ = self.__time_frame, side= tk.LEFT)
        self.__dinner_time_entry.pack(in_ = self.__time_frame, side= tk.RIGHT)
        self.__time_frame.pack()
        self.__price.pack(in_ = self.__left)
        self.__confirm_button.pack(pady = 10)
        self.update_card()

    def confirm(self):
        restaurant = Restaurant.get_instance()
        restaurant.set_name(self.__name_entry.get_content())
        restaurant.set_operating_time((self.__lunch_time_entry.get_content(), self.__dinner_time_entry.get_content()))
        restaurant.set_price(float(self.__price.get_content()))
        self.__controller.save()

        self.__lunch_time_entry.clear()
        self.__dinner_time_entry.clear()
        self.__name_entry.clear()
        self.__price.clear()
        self.update_card()

    def update_card(self):
        self.__controller.search()
        restaurant = Restaurant.get_instance()

        if self.__card is not None:
            self.__card.destroy()

        fields = dict(zip(restaurant.attr_labels(), restaurant.to_dict().values()))

        self.__card = Card("Restaurante", fields, lambda: ())
        self.__card.pack(in_ = self.__right, expand = True, ipadx = 10, ipady = 10)