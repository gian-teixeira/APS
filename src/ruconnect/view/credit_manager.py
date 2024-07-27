from model.user import Student
from tkinter import ttk
import tkinter as tk
from view.entry import Entry
from control.user import StudentController
from persistence.user import StudentPersistence
from model.session import Session

class CreditDisplay(ttk.Frame):
    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        assert isinstance(user, Student)

        self.credit_var = tk.StringVar()
        self.credit_frame = ttk.Frame(self)
        self.credit_text = ttk.Label(self.credit_frame, text = f'Créditos :')
        self.credit_value = ttk.Label(self.credit_frame, textvariable = self.credit_var)
        self.credits_entry = Entry("Insira a quantidade de cŕeditos")
        self.button = ttk.Button(self, text = 'Adicionar', command = self.compute_credits)

        self.credit_var.set(Session.get_user().credit)

    def pack(self, *args, **kwargs):
        self.credit_text.pack(side = tk.LEFT)
        self.credit_value.pack(side = tk.RIGHT)
        self.credit_frame.pack()
        self.credits_entry.pack()
        self.button.pack()
        super().pack(*args, **kwargs)

    def compute_credits(self):
        controller = StudentController(StudentPersistence())
        user = Session.get_user()
        user.credit += int(self.credits_entry.get_content())
        controller.delete(user.id)
        controller.save(user)
        self.credit_var.set(str(user.credit))
