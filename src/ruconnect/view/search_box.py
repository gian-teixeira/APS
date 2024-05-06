from view.entry import Entry

import tkinter as tk
from tkinter import ttk

class SearchBox(tk.Frame):
    def __init__(self, controller, label, selectmode = tk.MULTIPLE, selection_callback = None):
        super().__init__()
        self.controller = controller

        self.selectmode = selectmode
        self.select_box = tk.Frame(self)
        self.entry = Entry(label)
        self.update_button = ttk.Button(self, text = 'Atualizar', command = self.update)
        self.listbox = tk.Listbox(self.select_box, selectmode = selectmode, highlightthickness = 0)
        self.scroll = ttk.Scrollbar(self.select_box)

        self.listbox.bind("<<ListboxSelect>>", selection_callback)
        self.listbox.config(yscrollcommand = self.scroll.set)
        self.scroll.config(command = self.listbox.yview)
        self.entry.on_update(self.update)

    def search(self):
        entry_content = self.entry.get_content()
        return self.controller.search(None if entry_content == '' else entry_content)

    def curselection(self):
        items = self.search()
        selection = [items[int(index)] for index in self.listbox.curselection()]
        return selection
    
    def update(self, *args):
        self.listbox.delete(0, tk.END)
        for item in self.search():
            if item is None: continue
            self.listbox.insert(tk.END, str(item))

    def pack(self, *args, **kwargs):
        self.entry.pack(in_ = self, pady = 10, expand = True, fill = tk.X)
        self.listbox.pack(side = tk.LEFT, expand = True, fill = tk.BOTH)
        self.scroll.pack(side = tk.RIGHT, expand = True, fill = tk.Y)
        self.select_box.pack(expand = True, fill = tk.BOTH)
        self.update_button.pack(anchor = 'w', pady = 10)
        super().pack(*args, **kwargs)
        self.update()