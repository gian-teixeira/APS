from control import FeedbackController, DailyMenuController
from model.Feedback import Feedback
from view.Entry import Entry
from view.Selector import Selector
from view.Session import Session

import tkinter as tk
from tkinter import ttk

class FeedbackRegister(ttk.Frame):
    def __init__(self):
        super().__init__()

        self.controller = FeedbackController()
        self.error_label = {
            "already rated" : ttk.Label(self, 
                text = "Avaliação já realizada", foreground = "red", 
                relief = tk.GROOVE, justify = 'center'),
            "unknown menu" : ttk.Label(self, 
                text = "Cardápio não encontrado", foreground = "red",
                relief = tk.GROOVE, justify = 'center')
        }
        self.frame = ttk.Frame(self)
        self.date_menu_entry = Entry("Data da refeição")
        self.period_selector = Selector("Período", ["Almoço", "Jantar"])
        self.star_rating_selector = Selector(
            "Avaliação numérica", 
            ["⭐", "⭐⭐", "⭐⭐⭐", "⭐⭐⭐⭐", "⭐⭐⭐⭐⭐"])
        self.written_rating_entry = Entry("Avaliação escrita")
        self.confirm_button = ttk.Button(self.frame, 
            text = "Registrar", 
            command = self.confirm)
        
        self.frame.pack(expand = True, padx = 10, pady = 10)
        self.date_menu_entry.pack(in_ = self.frame)
        self.period_selector.pack(in_ = self.frame)
        self.star_rating_selector.pack(in_ = self.frame)
        self.written_rating_entry.pack(in_ = self.frame)
        self.confirm_button.pack(pady = 10)

    def confirm(self):
        self.error_label["already rated"].pack_forget()
        self.error_label["unknown menu"].pack_forget()

        menu_controller = DailyMenuController()
        date = self.date_menu_entry.get_content()

        if not menu_controller.read(date):
            self.error_label["unknown menu"].pack(expand = True)
            return

        feedback = Feedback(self.star_rating_selector.get_selection(),
            self.written_rating_entry.get_content(),
            self.date_menu_entry.get_content(),
            self.period_selector.get_selection(),
            Session.get_user().id)

        try:
            self.controller.create(feedback)
        except Exception as e:
            self.error_label["already rated"].pack(expand = True)
        else:
            self.date_menu_entry.clear()
            self.period_selector.clear()
            self.star_rating_selector.clear()
            self.written_rating_entry.clear()