import tkinter as tk
from tkinter import ttk, font as tk_font

class Card(ttk.Frame):
    def __init__(self, 
                 title_name : str,
                 data : dict,
                 delete_callback):
        super().__init__(relief = tk.GROOVE)
        self.__delete_callback = delete_callback

        title = ttk.Label(self, text = title_name, font = ('Helvetic 10 bold'))
        title.pack(expand = True)
        
        for key in data:
            line = tk.Frame(self)
            label = ttk.Label(line, text = f"{key} : ", font = ('Helvetic 10 normal'))
            value = ttk.Label(line, text = str(data[key]), font = ('Helvetic 10 italic'))

            label.pack(expand = True, side = tk.LEFT)
            value.pack(expand = True, side = tk.RIGHT)
            line.pack(expand = True)

        delete_button = ttk.Button(self, text = "Apagar", command = self.__delete)
        delete_button.pack(pady = 10)

    def __delete(self):
        self.__delete_callback()
        self.destroy()