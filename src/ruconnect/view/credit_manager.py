from model.user import Student
from tkinter import ttk
import tkinter as tk
from view.entry import Entry
from control.user import StudentController
from persistence.user import StudentPersistence

class CreditManager(ttk.Frame):
    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        assert isinstance(user, Student)

        self.user = user
        self.credit_var = tk.StringVar()
        self.credit_frame = ttk.Frame(self)
        self.credit_text = ttk.Label(self.credit_frame, text = f'Créditos :')
        self.credit_value = ttk.Label(self.credit_frame, textvariable = self.credit_var)
        self.credits_entry = Entry("Comprar créditos")
        self.button = ttk.Button(self, text = 'Adicionar', command = self.compute_credits)
        self.credit_var.set(user.credit)

        self.error_label = tk.Label(self, fg = 'red', wraplength = 200,
                                    text = 'Valor inválido. Insira um inteiro positivo!')

    def pack(self, *args, **kwargs):
        self.credit_text.pack(side = tk.LEFT)
        self.credit_value.pack(side = tk.RIGHT)
        self.credit_frame.pack(anchor = 'w')
        self.credits_entry.pack(in_ = self)
        self.button.pack(in_ = self, anchor = 'w', pady = 10)
        super().pack(*args, **kwargs)

    def compute_credits(self):
        try:
            credit_amount = int(self.credits_entry.get_content())
            assert(credit_amount > 0)
        except:
            self.error_label.pack(expand = False)
            return
        
        self.error_label.pack_forget()
        controller = StudentController(StudentPersistence())
        self.user = controller.search(self.user.id)[0]
        self.user.credit += credit_amount
        controller.delete(self.user.id)
        controller.save(self.user)
        self.credit_var.set(str(self.user.credit))
