from view.entry import Entry
import tkinter as tk
from tkinter import ttk

class SearchPanel(tk.Frame):
    def __init__(self, 
                 fields,
                 search_function,
                 selection_callback):
        super().__init__()
        self.__fields = fields
        self.__entries = dict()
        self.__search = search_function
        self.__selection_calback = selection_callback

        for field in fields: 
            self.__entries[field] = Entry(field)
            self.__entries[field].pack(in_ = self)

        confirm_button = ttk.Button(self, text = "Buscar", command = self.confirm)
        self.__response_list = tk.Listbox(self)
        response_scroll = tk.Scrollbar(self)

        confirm_button.pack(pady = 10)

        self.__response_list.config(yscrollcommand = response_scroll.set)
        response_scroll.config(command = self.__response_list.yview)

        self.__response_list.pack(side = tk.LEFT, fill = tk.X)
        response_scroll.pack(side = tk.RIGHT, fill = tk.Y)

    def confirm(self):
        search_values = [self.__entries[field].get_content() for field in self.__fields]
        self.__response_list.delete(0, tk.END)
        for value in self.__search(*search_values):
            self.__response_list.insert(tk.END, str(value))