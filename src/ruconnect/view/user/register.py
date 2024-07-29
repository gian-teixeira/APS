from persistence.user import StudentPersistence, AdministratorPersistence
from control.user import StudentController, AdministratorController
from model.user import Student, Administrator
from view.entry import Entry
from view.selector import Selector

import tkinter as tk
from tkinter import ttk

class UserRegister(ttk.Frame):
    def __init__(self):
        super().__init__()

        self.name = Entry("Nome")
        self.id = Entry("Id")
        self.password = Entry("Senha")
        self.type = Selector("Tipo", ("Estudante", "Administrador"))
        self.button = ttk.Button(self, text = "Registrar", command = self.confirm)
        self.error_label = ttk.Label(self, text = "Item já cadastrado", foreground = "red", 
                                     relief = tk.GROOVE, justify = 'center')

    def confirm(self):
        match self.type.get_selection():
            case "Administrador":
                user = Administrator(self.name.get_content(),
                                     self.id.get_content(),
                                     self.password.get_content())
                controller = AdministratorController(AdministratorPersistence())
            case "Estudante":
                user = Student(self.name.get_content(),
                               self.id.get_content(),
                               self.password.get_content(), 0)
                controller = StudentController(StudentPersistence())
         
        controller.save(user)
        self.name.clear()
        self.id.clear()
        self.password.clear()
        self.type.clear()

    def pack(self, *args, **kwargs):
        self.name.pack(in_ = self, expand = True)
        self.id.pack(in_ = self, expand = True)
        self.password.pack(in_ = self, expand = True)
        self.type.pack(in_ = self, expand = True)
        self.button.pack(in_ = self, pady = 10)
        super().pack(*args, **kwargs)

        