import tkinter as tk
from tkinter import ttk

class Selector(tk.Frame):
    def __init__(self, label_text, values, selection_callback = None, default = 0):
        super().__init__()
        self.content = tk.StringVar()
        
        label = ttk.Label(self, text = label_text)
        self.box = ttk.Combobox(self, textvariable = self.content)
        self.box["values"] = values
        self.box["state"] = "readonly"
        self.box.current(default)

        if selection_callback:
            self.box.bind("<<ComboboxSelected>>", selection_callback)
        
        label.pack(expand = True, fill = tk.BOTH)
        self.box.pack()

    def get_selection(self):
        return self.content.get()
    
    def clear(self):
        self.box.set("")