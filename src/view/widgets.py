import tkinter as tk
from tkinter import ttk

class TopicList(tk.Frame):
    INDENT_SIZE = 4

    def __init__(self,
                 master,
                 info):
        super().__init__(master)
        self.grid_columnconfigure(0, weight = 1)

        self.row = 0
        self.append(info)
        self.pack()
        
    def append(self, 
               info, 
               indent = 0):
        for item in info:
            text = (" " * indent * self.INDENT_SIZE) + str(item)
            label = ttk.Label(self, text = text, justify = tk.LEFT)
            label.grid(row = self.row, column = 0, sticky = tk.NSEW)
            self.row += 1
            
            if isinstance(info, dict): 
                self.append(info[item], indent = indent+1)

        

root = tk.Tk()

info = {
    "Procedural": { "C" },
    "Object Oriented" : {
        "C++", "Java", 
        "C#", "Python"
    }
}

TopicList(root, info)

root.mainloop()