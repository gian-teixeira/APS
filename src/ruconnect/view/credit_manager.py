from model.user import Student
from tkinter import ttk
import tkinter as tk
from view.entry import Entry
from control.user import UserController
from persistence.user import StudentPersistence

class CreditDisplay(ttk.Frame):
    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        assert isinstance(user, Student)

        self.label = ttk.Label(self, text = f'Créditos : {user.credit}')
        self.credits_entry = Entry("Insira a quantidade de cŕeditos")
        self.button = ttk.Button(self, text = 'Adicionar', )
        
        # user.set_credit(float(int(self.credits_entry.get_content())))

    def pack(self, *args, **kwargs):
        self.label.pack()
        self.credits_entry.pack()
        self.button.pack()
        super().pack(*args, **kwargs)

    def compute_credits(self, user):
        persistence = StudentPersistence()
        controller = UserController(persistence)
