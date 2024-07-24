from model.user import Student
from tkinter import ttk

class CreditDisplay(ttk.Frame):
    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        assert isinstance(user, Student)

        self.label = ttk.Label(self, text = f'Créditos : {user.credit}')
        self.button = ttk.Button(self, text = 'Adicionar')

    def pack(self, *args, **kwargs):
        self.label.pack()
        self.button.pack()
        super().pack(*args, **kwargs)