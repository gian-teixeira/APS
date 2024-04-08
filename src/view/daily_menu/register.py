from persistence.daily_menu import DailyMenuPersistence
from control.daily_menu import DailyMenuController
from model.daily_menu import DailyMenu
from view.entry import Entry
from view.selector import Selector
from persistence.edible import EdiblePersistence
from control.edible import EdibleController

import tkinter as tk
from tkinter import ttk

class DailyMenuRegister(ttk.Frame):
    def __init__(self):
        super().__init__()

        self.__persistence = DailyMenuPersistence()
        self.__controller = DailyMenuController(self.__persistence)

        self.__error_label = ttk.Label(self, 
                                       text = "Item já cadastrado",
                                       foreground = "red",
                                       relief = tk.GROOVE,
                                       justify = 'center')

        self.__frame = ttk.Frame(self)
        self.__entry = Entry("Data")
        self.__confirm_button = ttk.Button(self.__frame, text = "Registrar", command = self.confirm)
        self.__period_selector = Selector("Período", ["Almoço", "Jantar"])

        self.__right = ttk.Frame(self)
        self.__left = ttk.Frame(self)

        self.__response_list = tk.Listbox(self.__left, selectmode="multiple",highlightthickness = 0)
        self.__response_scroll = tk.Scrollbar(self.__left)

        #self.__response_list.bind("<<ListboxSelect>>", self.food_selection_callback())
        self.__response_list.config(yscrollcommand = self.__response_scroll.set)
        self.__response_scroll.config(command = self.__response_list.yview)

        self.__frame.pack(expand = True, padx = 10, pady = 10)
        self.__entry.pack(in_ = self.__frame)
        self.__confirm_button.pack(pady = 10)

        persistence = EdiblePersistence()
        controller = EdibleController(persistence)
        self.__edible_list = controller.search()

        for edible in self.__edible_list:
            self.__response_list.insert(tk.END, edible.get_name())

    def confirm(self):
        selected_edibles = [self.__edible_list[index]
                            for index in self.__response_list.curselection()]
        menu = DailyMenu()
        for edible in selected_edibles:
            match self.__period_selector.get_selection():
                case "Almoço": menu.add_edible(menu.get_lunch(), edible)
                case "Jantar": menu.add_edible(menu.get_dinner(), edible)

        self.__error_label.pack_forget()
        try:
            self.__search_result = self.__controller.save(edible)
        except:
            self.__error_label.pack(expand = True)
        else:
            self.__entry.clear()

    def food_select_callback(self):
        def callback(event):
            
            

            widget = event.widget
            index = widget.curselection()
            self.__selected_name = widget.get(index)
            selected = self.__search_result[index]

            if self.__card is not None:
                self.__card.destroy()

            card = Card("Card", selected.to_dict(), self.delete)
            card.pack(in_ = self.__right, expand = True, ipadx = 10, ipady = 10)
            self.__card = card

        return callback