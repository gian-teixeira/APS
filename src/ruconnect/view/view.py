from view.edible.panel import EdiblePanel
from view.daily_menu.panel import DailyMenuPanel
from view.restaurant.panel import RestaurantPanel

import tkinter as tk
from tkinter import ttk

class View(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("RUConnect")

        ttk.Style().theme_use('clam')

        self.panels = {
            "Comida": EdiblePanel(),
            "Cardápio": DailyMenuPanel(),
            "Restaurante": RestaurantPanel()
        }
        self.selected_panel = None

        self.sidebar = ttk.Frame(self)
        
        ttk.Label(self.sidebar, text = "RUConnect") \
            .pack(expand = True, anchor = "n", pady = 200)

        for panel_id in self.panels:
            button = ttk.Button(self.sidebar, text = panel_id,
                                command = self.panel_setter(panel_id))
            button.pack(expand = True, fill = tk.X)

        self.sidebar.pack(side = tk.LEFT, padx = 10, pady = 10)

        self.set_panel("Comida")

    def set_panel(self, panel_id):
        if self.selected_panel:
            self.panels[self.selected_panel].pack_forget()

        self.selected_panel = panel_id
        self.panels[self.selected_panel].pack(
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