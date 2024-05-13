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

        self.persistence = RestaurantPersistence()
        self.controller = RestaurantController(self.persistence)
        self.name_entry = Entry("Restaurante")
        self.price = Entry("Preço")
        self.left = tk.Frame(self)
        self.right = tk.Frame(self)
        self.time_frame = tk.Frame(self.left)
        self.lunch_time_entry = Entry("Horário Almoço")
        self.dinner_time_entry = Entry("Horário Jantar")
        self.card = None

        self.confirm_button = ttk.Button(self.left, text = "Registrar", command = self.confirm)

        self.left.pack(expand = True, side= tk.TOP)
        self.right.pack(expand = True, side= tk.BOTTOM)
        self.name_entry.pack(in_ = self.left)
        self.lunch_time_entry.pack(in_ = self.time_frame, side= tk.LEFT)
        self.dinner_time_entry.pack(in_ = self.time_frame, side= tk.RIGHT)
        self.time_frame.pack()
        self.price.pack(in_ = self.left)
        self.confirm_button.pack(pady = 10)
        self.update_card()

    def confirm(self):
        restaurant = Restaurant.get_instance()
        restaurant.set_name(self.name_entry.get_content())
        restaurant.set_operating_time((self.lunch_time_entry.get_content(), self.dinner_time_entry.get_content()))
        restaurant.set_price(float(self.price.get_content()))
        self.controller.save()

        self.lunch_time_entry.clear()
        self.dinner_time_entry.clear()
        self.name_entry.clear()
        self.price.clear()
        self.update_card()

    def update_card(self):
        self.controller.search()
        restaurant = Restaurant.get_instance()

        if self.card is not None:
            self.card.destroy()

        fields = dict(zip(restaurant.attr_labels(), restaurant.to_dict().values()))

        self.card = Card("Restaurante", fields, lambda: ())
        self.card.pack(in_ = self.right, expand = True, ipadx = 10, ipady = 10)