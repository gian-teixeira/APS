from view.edible.panel import EdiblePanel
from view.daily_menu.panel import DailyMenuPanel

import tkinter as tk
from tkinter import ttk

class View(tk.Tk):
    def __init__(self):
        super().__init__()

        ttk.Style().theme_use('clam')

        self.__panels = {
            "Comida": EdiblePanel(),
            "Cardápio": DailyMenuPanel()
        }
        self.__selected_panel = None

        self.__sidebar = ttk.Frame(self)

        # TODO : the buttons are mapping for the same window
        for panel_id in self.__panels:
            button = ttk.Button(self.__sidebar, text = panel_id,
                                command = lambda : self.set_panel(panel_id))
            button.pack(expand = True, fill = tk.X)

        self.__sidebar.pack(side = tk.LEFT, padx = 10, pady = 10)

        self.set_panel("Comida")

    def set_panel(self, panel_id):
        print(panel_id)

        if self.__selected_panel:
            self.__panels[self.__selected_panel].pack_forget()

        self.__selected_panel = panel_id
        self.__panels[self.__selected_panel].pack(
            in_ = self,
            expand = True,
            side = tk.RIGHT,
            fill = tk.BOTH,
            padx = 10,
            pady = 10)