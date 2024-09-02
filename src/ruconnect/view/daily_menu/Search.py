from control.controller.DailyMenuController import DailyMenuController
from view.Entry import Entry
from view.Card import Card
from view.SearchBox import SearchBox
from view.Session import Session
from view.provider.DailyMenuProvider import DailyMenuProvider

import tkinter as tk
from tkinter import ttk

class DailyMenuSearch(ttk.Frame):
    def __init__(self):
        super().__init__()

        self.controller = DailyMenuController()

        self.card = None
        self.selected_date = ""

        self.right = ttk.Frame(self)
        self.left = ttk.Frame(self)
        self.date_entry = Entry("Data")
        self.search = SearchBox(
            self.controller, 
            DailyMenuProvider,
            ["Data"],
            tk.SINGLE,
            self.selection_callback())

    def delete(self):
        self.controller.delete(self.selected)
        self.search.update()

    def selection_callback(self):
        def callback(event):
            if len(self.search.curselection()) == 0: 
                return
            
            self.selected = self.search.curselection()[0]
            
            if self.card is not None:
                self.card.destroy()
            
            card = Card(DailyMenuProvider, self.selected, self.delete)
            card.pack(in_ = self.right, expand = True, ipadx = 10, ipady = 10)
            self.card = card

        return callback

    def pack(self, *args, **kwargs):
        self.search.pack(in_ = self.left)
        self.left.pack(expand = True, side = tk.TOP, padx = 10, pady = 10)
        self.right.pack(expand = True, side = tk.BOTTOM, padx = 10, pady = 10)
        super().pack(*args, **kwargs)