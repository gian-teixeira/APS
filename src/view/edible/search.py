from persistence.edible import EdiblePersistence
from control.edible import EdibleController
from view.entry import Entry
from view.card import Card

import tkinter as tk
from tkinter import ttk

class EdibleSearch(ttk.Frame):
    def __init__(self):
        super().__init__()

        self.__persistence = EdiblePersistence()
        self.__controller = EdibleController(self.__persistence)

        self.__card = None
        self.__selected_name = ""

        self.__right = ttk.Frame(self)
        self.__left = ttk.Frame(self)
        self.__entry = Entry("Nome")
        self.__confirm_button = ttk.Button(self.__left, text = "Buscar", command = self.confirm)
        self.__response_list = tk.Listbox(self.__left, highlightthickness = 0)
        self.__response_scroll = tk.Scrollbar(self.__left)

        self.__response_list.bind("<<ListboxSelect>>", self.selection_callback())
        self.__response_list.config(yscrollcommand = self.__response_scroll.set)
        self.__response_scroll.config(command = self.__response_list.yview)

        self.__left.pack(expand = True, side = tk.TOP, padx = 10, pady = 10)
        self.__right.pack(expand = True, side = tk.BOTTOM, padx = 10, pady = 10)
        self.__entry.pack(in_ = self.__left)
        self.__confirm_button.pack(pady = 10)
        self.__response_list.pack(side = tk.LEFT, fill = tk.X)
        self.__response_scroll.pack(side = tk.RIGHT, fill = tk.Y)

    def confirm(self):
        edible_name = self.__entry.get_content()
        self.__search_result = self.__controller.search_by_name(edible_name)
        self.__response_list.delete(0, tk.END)
        for value in self.__search_result:
            self.__response_list.insert(tk.END, str(value))

    def delete(self):
        print(self.__selected_name)
        self.__controller.delete_by_name(self.__selected_name)
        self.confirm()

    def selection_callback(self):
        def callback(event):
            widget = event.widget
            
            if len(widget.curselection()) == 0:
                return

            index = int(widget.curselection()[0])
            self.__selected_name = widget.get(index)
            selected = self.__search_result[index]

            if self.__card is not None:
                self.__card.destroy()

            fields = dict(zip(selected.attr_labels(), selected.to_dict().values()))

            card = Card("Comida", fields, self.delete)
            card.pack(in_ = self.__right, expand = True, ipadx = 10, ipady = 10)
            self.__card = card

        return callback