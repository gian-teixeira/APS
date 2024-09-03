from control import StudentConsumptionController, DailyMenuController, StudentController
from model.StudentConsumption import StudentConsumption
from view.Entry import Entry
from view.Selector import Selector
from view.Session import Session
from model.User import Student, Administrator

import tkinter as tk
from tkinter import ttk

class StudentConsumptionRegister(ttk.Frame):
    def __init__(self):
        super().__init__()

        self.error_label = {
            "unknown menu" : ttk.Label(self, 
                text = "Cardápio não encontrado", foreground = "red",
                relief = tk.GROOVE, justify = 'center'),
            "unknown user" : ttk.Label(self, 
                text = "Aluno não encontrado", foreground = "red",
                relief = tk.GROOVE, justify = 'center')
        }
        
        self.frame = ttk.Frame(self)
        self.date_menu_entry = Entry("Data da refeição")
        self.period_selector = Selector("Período da refeição", ["Almoço", "Jantar"])
        self.student_id_entry = Entry("Id do aluno")
        if isinstance(Session.get_user(), Student):
            self.student_id_entry.set(Session.get_user().id)
            self.student_id_entry.entry.config(state='disabled')
        self.confirm_button = ttk.Button(self.frame, text = "Registrar", command = self.confirm)
        
        self.frame.pack(expand = True, padx = 10, pady = 10)
        self.student_id_entry.pack(in_ = self.frame)
        self.date_menu_entry.pack(in_ = self.frame)
        self.period_selector.pack(in_ = self.frame)
        self.confirm_button.pack(pady = 10)

    def confirm(self):
        self.error_label["unknown menu"].pack_forget()
        self.error_label["unknown user"].pack_forget()
        
        menu_controller = DailyMenuController()
        consumption_controller = StudentConsumptionController()
        student_controller = StudentController()

        date = self.date_menu_entry.get_content()
        student_id = self.student_id_entry.get_content()
        menu = menu_controller.read(date)
        student = student_controller.read(student_id)

        if not student:
            self.error_label["unknown user"].pack(expand = True)
            return

        if not menu:
            self.error_label["unknown menu"].pack(expand = True)
            return
        
        period = self.period_selector.get_selection()
        student = student_controller.read(self.student_id_entry.get_content())[0]
        consumption = consumption_controller.read(student.id)
        if not consumption:
            consumption = StudentConsumption(student.id, 1, [(date,period)])
            consumption_controller.create(consumption)
        else:
            consumption = consumption[0]
            consumption.spent_credits += 1
            consumption.days_attended += [(date,period)]
            consumption_controller.update(consumption)
        student.credit += 1
        student_controller.update(student)

        self.date_menu_entry.clear()
        self.period_selector.clear()
        self.student_id_entry.clear()