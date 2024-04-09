import tkinter as tk
from tkinter import ttk

class Selector(tk.Frame):
    def __init__(self, label_text, values):
        super().__init__()
        self.__content = tk.StringVar()
        
        label = ttk.Label(self, text = label_text)
        self.__box = ttk.Combobox(self, textvariable = self.__content)
        self.__box["values"] = values
        self.__box["state"] = "readonly"
        
        label.pack(expand = True, fill = tk.BOTH)
        self.__box.pack()

    def get_selection(self):
        return self.__content.get()
    
    def clear(self):
        self.__box.set("")