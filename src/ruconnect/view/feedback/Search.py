from control.controller.FeedbackController import FeedbackController
from view.SearchBox import SearchBox
from view.Card import Card
from view.Session import Session
from view.provider.FeedbackProvider import FeedbackProvider

import tkinter as tk
from tkinter import ttk

class FeedbackSearch(ttk.Frame):
    def __init__(self):
        super().__init__()

        self.controller = FeedbackController()
        self.card = None
        self.selected_name = None
        self.right = ttk.Frame(self)
        self.left = ttk.Frame(self)
        self.search = SearchBox(
            self.controller, FeedbackProvider,
            ["Id", "Data", "Período"], tk.SINGLE, self.selection_callback())
        
        self.left.pack(expand = True, side = tk.TOP, padx = 10, pady = 10)
        self.right.pack(expand = True, side = tk.BOTTOM, padx = 10, pady = 10)
        self.search.pack(in_ = self.left, fill = tk.BOTH)

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
            
            card = Card(FeedbackProvider, self.selected, self.delete)
            card.pack(in_ = self.right, expand = True, ipadx = 10, ipady = 10)
            self.card = card

        return callback