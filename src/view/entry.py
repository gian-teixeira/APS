import tkinter as tk
from tkinter import ttk

class Entry(tk.Frame):
    def __init__(self, 
                 label_text):
        super().__init__()
        self.__content = tk.StringVar()
        
        label = ttk.Label(self, text = label_text)
        self.__entry = ttk.Entry(self, textvariable = self.__content)
        
        label.pack(expand = True, fill = tk.BOTH)
        self.__entry.pack()

    def get_content(self):
        return self.__content.get()
    
    def clear(self):
        self.__entry.delete(0, tk.END)