import tkinter as tk
from tkinter import ttk

class Entry(tk.Frame):
    def __init__(self, label_text):
        super().__init__()
        self.content = tk.StringVar()
        
        label = ttk.Label(self, text = label_text)
        self.entry = ttk.Entry(self, textvariable = self.content)
        
        label.pack(expand = True, fill = tk.BOTH)
        self.entry.pack(expand = True, fill = tk.X)

    def get_content(self):
        return self.content.get()
    
    def clear(self):
        self.entry.delete(0, tk.END)
    
    def on_update(self, func):
        self.content.trace_add('write', func)