from persistence.edible import EdiblePersistence
from control.edible import EdibleController
from view.search_box import SearchBox
from view.card import Card
from model.session import Session

import tkinter as tk
from tkinter import ttk

class EdibleSearch(ttk.Frame):
    def __init__(self):
        super().__init__()

        self.persistence = EdiblePersistence()
        self.controller = EdibleController(self.persistence)
        self.card = None
        self.selected_name = ""
        self.right = ttk.Frame(self)
        self.left = ttk.Frame(self)
        self.search = SearchBox(EdibleController(EdiblePersistence()), ["Alimentos"], 
                                tk.SINGLE, self.selection_callback())
        
        self.left.pack(expand = True, side = tk.TOP, padx = 10, pady = 10)
        self.right.pack(expand = True, side = tk.BOTTOM, padx = 10, pady = 10)
        self.search.pack(in_ = self.left, fill = tk.BOTH)

    def delete(self):
        self.controller.delete(self.selected_name)
        self.search.update()

    def selection_callback(self):
        def callback(event):
            selected = self.search.curselection()

            if len(selected) == 0: return
            selected = selected[0]

            if self.card is not None:
                self.card.destroy()

            fields = dict(zip(selected.attr_labels(), selected.to_dict().values()))

            card = Card(Session.get_user(), "Comida", fields, self.delete)
            card.pack(in_ = self.right, expand = True, ipadx = 10, ipady = 10)
            self.card = card

        return callback