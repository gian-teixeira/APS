from view.entry import Entry
from view.card.card import Card
import tkinter as tk
from tkinter import ttk

class SearchPanel(ttk.Frame):
    def __init__(self, 
                 search_field : tuple,
                 delete_function,
                 card_type : type = None):
        super().__init__()

        self.__search_key = search_field[0] 
        self.__search_function = search_field[1]
        self.__delete_function = delete_function
        self.__card = None
        self.__selected_id = None

        self.__right = ttk.Frame(self)
        self.__left = ttk.Frame(self)
        self.__entry = Entry(self.__search_key)
        self.__confirm_button = ttk.Button(self.__left, text = "Buscar", command = self.confirm)
        self.__response_list = tk.Listbox(self.__left, highlightthickness = 0)
        self.__response_scroll = tk.Scrollbar(self.__left)

        self.__response_list.bind("<<ListboxSelect>>", self.selection_callback())
        self.__response_list.config(yscrollcommand = self.__response_scroll.set)
        self.__response_scroll.config(command = self.__response_list.yview)

        self.__left.pack(expand = True, side = tk.LEFT, padx = 10, pady = 10)
        self.__right.pack(expand = True, side = tk.RIGHT, padx = 10, pady = 10)
        self.__entry.pack(in_ = self.__left)
        self.__confirm_button.pack(pady = 10)
        self.__response_list.pack(side = tk.LEFT, fill = tk.X)
        self.__response_scroll.pack(side = tk.RIGHT, fill = tk.Y)

    def confirm(self):
        search_value = self.__entry.get_content()
        self.__search_result = self.__search_function(search_value)
        for value in self.__search_result:
            self.__response_list.insert(tk.END, str(value))

    def delete(self):
        print(self.__delete_function)
        self.__delete_function(self.__selected_id)

    def selection_callback(self):
        def callback(event):
            widget = event.widget
            self.__selected_id = widget.curselection()[0]
            selected = self.__search_result[self.__selected_id]

            if self.__card is not None:
                self.__card.destroy()

            card = Card("Card", selected.to_dict(), self.delete)
            card.pack(in_ = self.__right, expand = True, ipadx = 10, ipady = 10)
            self.__card = card

        return callback
