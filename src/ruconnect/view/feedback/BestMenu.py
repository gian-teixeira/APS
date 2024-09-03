from control import FeedbackController, DailyMenuController
from model.Feedback import Feedback
from view.Entry import Entry
from view.Selector import Selector
from view.Session import Session

from collections import defaultdict
import tkinter as tk
from tkinter import ttk

class FeedbackBestMenu(ttk.Frame):
    def __init__(self):
        super().__init__()

        self.controller = FeedbackController()
        self.frame = ttk.Frame(self)
        self.update()

    def update(self):
        self.frame.pack_forget()
        self.frame = ttk.Frame(self)
        self.frame.pack(expand = True, padx = 10, pady = 10)
        
        count = defaultdict(lambda : 0)
        for feedback in self.controller.read():
            id = f"{feedback.menu_date} {feedback.menu_period}"
            count[id] += len(feedback.star_rating)
        
        if len(count.items()):
            best_menu = max(count.items(), key = lambda pair: pair[1])
            ttk.Label(self.frame, text = "Melhor cardápio : "+str(best_menu[0])).pack()
            ttk.Label(self.frame, text = "Avaliação : "+str(best_menu[1])).pack()