from control import RestaurantController
from view.provider.RestaurantProvider import RestaurantProvider
from model import Restaurant
from view.Entry import Entry
from view.Card import Card
from view.Session import Session

import tkinter as tk
from tkinter import ttk

class RestaurantRegister(ttk.Frame):
    def __init__(self):
        super().__init__()

        self.controller = RestaurantController()

        self.name_entry = Entry("Restaurante")
        self.price_entry = Entry("Preço")
        self.lunch_time_entry = Entry("Horário Almoço")
        self.dinner_time_entry = Entry("Horário Jantar")
        self.card = None

        self.confirm_button = ttk.Button(self, text = "Registrar", command = self.confirm)

        self.name_entry.pack(in_ = self)
        self.lunch_time_entry.pack(in_ = self)
        self.dinner_time_entry.pack(in_ = self)
        self.price_entry.pack(in_ = self)
        self.confirm_button.pack(pady = 10)
        self.update_card()

    def confirm(self):
        try: restaurant = self.controller.read()[0]
        except: restaurant = Restaurant.get_instance()

        restaurant.name = self.name_entry.get_content()
        restaurant.operating_time = (
            self.lunch_time_entry.get_content(), 
            self.dinner_time_entry.get_content())
        restaurant.price = float(self.price_entry.get_content())

        try: self.controller.update(restaurant)
        except: self.controller.create(restaurant)

        self.lunch_time_entry.clear()
        self.dinner_time_entry.clear()
        self.name_entry.clear()
        self.price_entry.clear()
        self.update_card()

    def update_card(self):
        try: restaurant = self.controller.read()[0]
        except: restaurant = Restaurant.get_instance()
        
        if self.card is not None:
            self.card.destroy()
        
        self.card = Card(RestaurantProvider, restaurant, lambda : None)
        self.card.pack(in_ = self, expand = True, ipadx = 10, ipady = 10)