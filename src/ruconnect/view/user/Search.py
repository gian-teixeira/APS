from view.SearchBox import SearchBox
from view.Selector import Selector
from view.user.Info import UserInfoDisplay
from view.provider.UserProvider import AdministratorProvider, StudentProvider
from control import StudentController, AdministratorController
from model import Administrator, Student
from view.Session import Session

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
            self.controller = AdministratorController()
            self.provider = AdministratorProvider()
        else:
            self.user_type = Student
            self.controller = StudentController()
            self.provider = StudentProvider()
        
        if self.search: self.search.pack_forget()
        self.search = SearchBox(
            self.controller, self.provider, 
            ["CPF"], tk.SINGLE,
            self.search_selection_callback)
        
        self.search.pack(in_ = self)
    
    def search_selection_callback(self, event):
        user = self.search.curselection()[0]
        user = self.controller.read(user.id)[0]

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
        user_id = self.search.curselection()[0]
        self.controller.delete(user_id)
        self.selection_card.pack_forget()
        self.search.update()

    def pack(self, *args, **kwargs):
        self.type_selector.pack(in_ = self)
        self.type_selection_callback(None)
        super().pack(*args, **kwargs)