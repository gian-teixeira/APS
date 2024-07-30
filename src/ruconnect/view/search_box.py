from view.entry import Entry

import tkinter as tk
from tkinter import ttk

class SearchBox(ttk.Frame):
    def __init__(self, controller, entries, selectmode = tk.MULTIPLE, selection_callback = None):
        super().__init__()
        assert(len(entries) > 0)
        
        self.controller = controller
        self.selectmode = selectmode
        self.select_box = ttk.Frame(self)
        self.update_button = ttk.Button(self, text = 'Atualizar', command = self.update)
        self.listbox = tk.Listbox(self.select_box, selectmode = selectmode, highlightthickness = 0)
        self.scroll = ttk.Scrollbar(self.select_box)
        self.entries = list()

        for label in entries:
            entry = Entry(label)
            entry.on_update(self.update)
            self.entries.append(entry)
        self.listbox.bind("<<ListboxSelect>>", selection_callback)
        self.listbox.config(yscrollcommand = self.scroll.set)
        self.scroll.config(command = self.listbox.yview)

    def search(self):
        search_content = []
        for entry in self.entries:
            content = entry.get_content().strip()
            search_content.append(content if len(content) else '.*')
        search_content = '/'.join(search_content)
        if(search_content == ''): search_content = None
        return self.controller.search(search_content)
    
    def entry_values(self):
        return [entry.get_content() for entry in self.entries]

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
        for entry in self.entries:
            entry.pack(in_ = self, pady = 10, expand = True, fill = tk.X)
        self.listbox.pack(side = tk.LEFT, expand = True, fill = tk.BOTH)
        self.scroll.pack(side = tk.RIGHT, expand = True, fill = tk.Y)
        self.select_box.pack(expand = True, fill = tk.BOTH)
        self.update_button.pack(anchor = 'w', pady = 10)
        super().pack(*args, **kwargs)
        self.update()