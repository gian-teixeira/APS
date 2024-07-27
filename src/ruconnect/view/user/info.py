from view.credit_manager import CreditManager
from model.user import Student
from tkinter import ttk

class UserInfoDisplay(ttk.Frame):
    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.id_label = ttk.Label(self, text = f'Id : {user.id}')
        self.name_label = ttk.Label(self, text = f'Nome : {user.name}')
        self.credit_area = CreditManager(user, self) if isinstance(user, Student) else None
        
    def pack(self, *args, **kwargs):
        self.id_label.pack(anchor = 'w')
        self.name_label.pack(anchor = 'w')
        if self.credit_area is not None:
            self.credit_area.pack()
        super().pack(*args, **kwargs)