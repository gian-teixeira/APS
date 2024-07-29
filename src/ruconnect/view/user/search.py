from persistence.feedback import FeedbackPersistence
from control.feedback import FeedbackController
from control.user import StudentController, AdministratorController
from persistence.user import StudentPersistence, AdministratorPersistence
from view.search_box import SearchBox
from view.selector import Selector
from model.user import Administrator, Student
from view.user.info import UserInfoDisplay
from model.session import Session

import tkinter as tk
from tkinter import ttk

class UserSearch(ttk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.type_selector = Selector("Tipo", ["Administrador", "Aluno"],
                                      selection_callback = self.type_selection_callback,
                                      default = 0)
        self.selection_card = None
        self.search = None

    def type_selection_callback(self, event):
        if self.type_selector.get_selection() == "Administrador":
            self.user_type = Administrator
            self.controller = AdministratorController(AdministratorPersistence())
        else:
            self.user_type = Student
            self.controller = StudentController(StudentPersistence())
        
        if self.search:
            self.search.pack_forget()
        self.search = SearchBox(self.controller, ["Id"], tk.SINGLE,
                                self.search_selection_callback)
        
        self.search.pack(in_ = self)
    
    def search_selection_callback(self, event):
        user_id = self.search.entry_values()[0]
        user = self.controller.search(user_id)[0]

        if self.selection_card:
            self.selection_card.pack_forget()
        self.selection_card = ttk.Frame(self)
        self.user_info = UserInfoDisplay(user, self.selection_card)
        self.delete_button = ttk.Button(self.selection_card,
                                        text = "Delete",
                                        command = self.delete_selection_callback)

        self.user_info.pack()
        self.delete_button.pack()
        self.selection_card.pack()
    
    def delete_selection_callback(self):
        user_id = self.search.entry_values()[0]
        self.controller.delete(user_id)
        self.selection_card.pack_forget()
        self.search.update()

    def pack(self, *args, **kwargs):
        self.type_selector.pack(in_ = self)
        self.type_selection_callback(None)
        super().pack(*args, **kwargs)
    
    '''def confirm(self):
        edible_name = self.entry.get_content()
        self.search_result = self.controller.search_by_name(edible_name)
        self.response_list.delete(0, tk.END)
        for value in self.search_result:
            self.response_list.insert(tk.END, str(value))

    def delete(self):
        self.controller.delete_by_name(self.selected_name)
        self.confirm()

    def selection_callback(self):
        def callback(event):
            selected = self.search.curselection()

            if len(selected) == 0: return
            selected = selected[0]

            if self.card is not None:
                self.card.destroy()

            fields = dict(zip(selected.attr_labels(), selected.to_dict().values()))

            card = Card("Comida", fields, self.delete)
            card.pack(in_ = self.right, expand = True, ipadx = 10, ipady = 10)
            self.card = card

        return callback'''