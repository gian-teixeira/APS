from view.edible.panel import EdiblePanel
from view.daily_menu.panel import DailyMenuPanel
from view.restaurant.panel import RestaurantPanel
from view.feedback.panel import FeedbackPanel
from view.user.panel import UserPanel
from model.user import User, Administrator
from model.session import Session
from view.user.info import UserInfoDisplay

import tkinter as tk
from tkinter import ttk

class View(tk.Tk):
    def __init__(self):
        super().__init__()
        ttk.Style().theme_use('clam')
        self.title("RUConnect")
        
        self.panels = {
            "Comida": (EdiblePanel(), User),
            "Cardápio": (DailyMenuPanel(), User),
            "Avaliação": (FeedbackPanel(), User),
            "Usuário": (UserPanel(), Administrator),
            "Restaurante": (RestaurantPanel(), Administrator),
        }
        self.selected_panel = None
        self.sidebar = ttk.Frame(self)
        
        ttk.Label(self.sidebar, text = "RUConnect").pack(anchor = "n")
        user = Session.get_user()
        self.credits = None

        self.user_area = UserInfoDisplay(user, self.sidebar)
        self.user_area.pack(pady = 10)
        
        self.button_area = ttk.Frame(self.sidebar)
        
        for panel_id in self.panels:
            if not isinstance(user, self.panels[panel_id][1]): continue
            button = ttk.Button(self.button_area, text = panel_id,
                                command = self.panel_setter(panel_id))
            button.pack(expand = True, fill = tk.X)
        
        self.button_area.pack(expand = True, fill = tk.X, anchor = 's', pady = 30)
        self.sidebar.pack(fill = tk.Y, side = tk.LEFT, padx = 10, pady = 10)
        self.set_panel("Comida")

    def set_panel(self, panel_id):
        if self.selected_panel:
            self.panels[self.selected_panel][0].pack_forget()

        self.selected_panel = panel_id
        self.panels[self.selected_panel][0].pack(
            in_ = self,
            expand = True,
            side = tk.RIGHT,
            fill = tk.BOTH,
            padx = 10,
            pady = 10)
    
    def panel_setter(self, panel_id):
        def setter():
            self.set_panel(panel_id)
        return setter