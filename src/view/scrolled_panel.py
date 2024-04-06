import tkinter as tk

class ScrolledPanel(tk.Frame):
    def __init__(self):
        super().__init__()

        self.__frame = tk.Frame(self, background = "green")
        self.__scroll_bar = tk.Scrollbar(self, orient = tk.VERTICAL)
        self.__canvas = tk.Canvas(self, yscrollcommand = self.__scroll_bar.set)

        self.__canvas.create_window(0, 0, window = self.__frame)
        self.__canvas.configure(relief = tk.FLAT,
                         background = "red")
        self.__canvas.pack(expand = True, fill = tk.BOTH, side = tk.LEFT)
        
        self.__scroll_bar.config(command = self.__canvas.yview)
        self.__scroll_bar.lift(self.__frame)
        self.__scroll_bar.pack(fill = tk.Y, side = tk.RIGHT)

        self.__frame.bind("<Configure>", self.__resize)

        tmp = tk.Label(self.__frame, text = "Prenatzi")

    def __resize(self, event):
        size = (self.__frame.winfo_reqwidth(), self.__frame.winfo_reqheight())
        self.__canvas.config(scrollregion = (0,0) + size)