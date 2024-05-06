from persistence.daily_menu import DailyMenuPersistence
from control.daily_menu import DailyMenuController
from view.entry import Entry
from view.card import Card
from view.search_box import SearchBox

import tkinter as tk
from tkinter import ttk

class DailyMenuSearch(ttk.Frame):
    def __init__(self):
        super().__init__()

        self.persistence = DailyMenuPersistence()
        self.controller = DailyMenuController(self.persistence)

        self.card = None
        self.selected_date = ""

        self.right = ttk.Frame(self)
        self.left = ttk.Frame(self)
        self.date_entry = Entry("Data")
        self.search = SearchBox(DailyMenuController(DailyMenuPersistence()), "Data")

    def confirm(self):
        date = self.date_entry.get_content()
        self.search_result = self.controller.search(date)
        self.response_list.delete(0, tk.END)
        for value in self.search_result:
            self.response_list.insert(tk.END, str(value))

    def delete(self):
        self.controller.delete(self.selected_date)
        self.confirm()

    def selection_callback(self):
        def callback(event):
            widget = event.widget

            if len(widget.curselection()) == 0:
                return
            
            index = int(widget.curselection()[0])
            self.selected_date = widget.get(index)
            selected = self.search_result[index]
            
            if self.card is not None:
                self.card.destroy()

            fields = dict(zip(selected.attr_labels(), selected.to_dict().values()))

            card = Card("Cardápio do dia", fields, self.delete)
            card.pack(in_ = self.right, expand = True, ipadx = 10, ipady = 10)
            self.card = card

        return callback

    def pack(self, *args, **kwargs):
        self.search.pack(in_ = self.left)
        self.left.pack(expand = True, side = tk.TOP, padx = 10, pady = 10)
        self.right.pack(expand = True, side = tk.BOTTOM, padx = 10, pady = 10)
        super().pack(*args, **kwargs)