import tkinter as tk
from tkinter import ttk
from datetime import datetime, time
from typing import NewType
from dataclasses import dataclass

@dataclass
class Meal:
    main_course : str = "..."
    side_dish : str = "..."
    salad : str = "..."
    juice : str = "..."
    dessert : str = "..."



class Restaurant:
    phone : int = 33718990
    email : str = "ru@ufsj.edu.br"
    operating_time : tuple = ("11:00", "13:30")
    credit_price : float = 2.75 

class Interface(tk.Tk):
    _instance = None

    def __init__(self):
        super().__init__()

        self.grid_rowconfigure(0, weight=2)
        self.grid_columnconfigure(0, weight=3)
        self.grid_columnconfigure(1, weight=7)

        self.workspace = tk.Frame(self, bg = "red")
        self.side = tk.Frame(self, bg = "blue")

        self.workspace.grid(column = 1, sticky = tk.NSEW)
        self.side.grid(column = 0, sticky = tk.NSEW)

    @classmethod
    def instance(cls):
        if cls._instance is None:
            cls._instance = cls()
            print('creating instance')
        return cls._instance




class RestaurantView(tk.Frame):

    def __init__(self, 
                 master : tk.Misc):
        super().__init__(master)
        
        self.grid_rowconfigure(0, weight = 1)
        self.grid_columnconfigure(0, weight = 1)
        self.grid_columnconfigure(1, weight = 20)

    @staticmethod
    def get_menu() -> ttk.Frame:
        table = ttk.Frame(borderwidth = 2)
        
        style = ttk.Style(table)
        style.configure("TLabel", 
                        borderwidth = 1, 
                        relief = "solid",
                        padding = (10,10))
        style.configure("Highlight.TLabel", background = "lightgreen")
        style.configure("Group.TLabel", background = "gray")

        header = ["Prato principal", "Acompanhamento", "Salada", "Suco", "Sobremesa"]
        table_data = [header, header]

        for i in range(len(table_data)):
            if i > 0:
                period = ttk.Label(table, 
                                   text = "Janta" if i%2 == 0 else "Almoço",
                                   style = "Group.TLabel")
                period.grid(row = i, column = 0, sticky = tk.NSEW)
            for j in range(len(table_data[i])):
                label = ttk.Label(table, 
                                  text = table_data[i][j], 
                                  style = "TLabel" if i else "Highlight.TLabel")
                label.grid(row = i, column = j+1, sticky = tk.NSEW)

        return table
        
        


    '''@staticmethod
    def info_table():
        info = {
            "Horário de funcionamento": [],
            "Almoço": Aberto de {Restaurant.operating_time[0]}h às f{Restaurant.operating_time[1]}",
            "Preço da refeição": [Restaurant.credit_price],
            "Telefone": [Restaurant.phone],
            "Email": [Restaurant.email]
        }
        
        container = ttk.Frame()

        for i,label in enumerate(info):
            row_name = ttk.Label(container,
                                 text = label,
                                 font = 'Helvetica 12 bold',
                                 justify = tk.LEFT)
            row_name.grid(row = i, 
                          column = 0, 
                          sticky = tk.NSEW,
                          padx = 10)
            
            for j,val in enumerate(info[label]):
                col = ttk.Label(container,
                                text = str(val),
                                font = 'Helvetica 12',
                                justify = tk.LEFT)
                col.grid(row = i,
                         column = j+1,
                         sticky = tk.NSEW,
                         padx = 10) 
                
        return container'''


if __name__ == "__main__":
    interface = Interface.instance() 

    menu = RestaurantView.get_menu()
    menu.pack(in_ = interface.workspace)

    interface.mainloop()

