from view.Entry import Entry
from view.Session import Session
import tkinter as tk
from tkinter import ttk

class SearchBox(ttk.Frame):
    def __init__(self, 
                 controller,
                 provider,
                 entry_labels,
                 selectmode = tk.MULTIPLE, 
                 selection_callback = None):
        super().__init__()
        
        self.controller = controller
        self.provider = provider
        self.selectmode = selectmode
        self.select_box = ttk.Frame(self)
        self.update_button = ttk.Button(self, text = 'Atualizar', command = self.update)
        self.listbox = tk.Listbox(self.select_box, selectmode = selectmode, highlightthickness = 0)
        self.scroll = ttk.Scrollbar(self.select_box)
        self.entries = [Entry(label) for label in entry_labels]
        
        for entry in self.entries:
            entry.on_update(self.update)
        self.listbox.bind("<<ListboxSelect>>", selection_callback)
        self.listbox.config(yscrollcommand = self.scroll.set)
        self.scroll.config(command = self.listbox.yview)

    def search(self):
        id = ' '.join([entry.get_content() for entry in self.entries])
        if id.strip() == '': id = None
        content = self.controller.read(id)
        return content if content else []
    
    def entry_value(self):
        return self.entries[0].get_content()

    def curselection(self):
        items = self.search()
        selection = [items[int(index)] for index in self.listbox.curselection()]
        return selection
    
    def update(self, *args):
        self.listbox.delete(0, tk.END)
        for item in self.search():
            if item is None: continue
            self.listbox.insert(tk.END, self.provider.label(item))

    def pack(self, *args, **kwargs):
        for entry in self.entries:
            entry.pack(in_ = self, pady = 10, expand = True, fill = tk.X)
        self.listbox.pack(side = tk.LEFT, expand = True, fill = tk.BOTH)
        self.scroll.pack(side = tk.RIGHT, expand = True, fill = tk.Y)
        self.select_box.pack(expand = True, fill = tk.BOTH)
        self.update_button.pack(anchor = 'w', pady = 10)
        super().pack(*args, **kwargs)
        self.update()