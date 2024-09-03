from model.User import Administrator
from view.Session import Session
import tkinter as tk
from tkinter import ttk

class Card(ttk.Frame):
    def __init__(self, 
                 provider, 
                 item, 
                 delete_callback, 
                 deleter_type = Administrator):
        super().__init__(relief = tk.GROOVE)
        self.delete_callback = delete_callback
        
        user = Session.get_user()
        title = ttk.Label(self, text = provider.label(item), font = ('Helvetic 10 bold'))
        title.pack(expand = True)
        
        for key,value in provider.info(item):
            line = ttk.Frame(self)
            label = ttk.Label(line, text = f"{key} : ", font = ('Helvetic 10 normal'))
            value = ttk.Label(line, text = str(value), font = ('Helvetic 10 italic'))

            label.pack(expand = True, side = tk.LEFT)
            value.pack(expand = True, side = tk.RIGHT)
            line.pack(expand = True)

        if isinstance(user, deleter_type):
            delete_button = ttk.Button(self, text = "Apagar", command = self.__delete)
            delete_button.pack(pady = 10)

    def __delete(self):
        self.delete_callback()
        self.destroy()