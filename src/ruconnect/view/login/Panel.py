from control.controller.UserController import AdministratorController, StudentController
from view.Entry import Entry
from view.Selector import Selector
from model.User import Administrator
from tkinter import Tk, StringVar, ttk, font
        
class LoginPanel(Tk):
    def __init__(self, enter_callback):
        super().__init__()
        ttk.Style().theme_use('clam')
        self.title("RUConnect - Login")
        
        self.container = ttk.Frame(self)
        self.wrapper = ttk.Frame(self.container)
        self.id = Entry("Id")
        self.password = Entry("Password")
        self.type = Selector("Tipo", ("Estudante", "Administrador"))
        self.button = ttk.Button(self, text = "Entrar", command = self.attempt)
        self.error_text = StringVar()
        self.error_label = ttk.Label(self.container, textvariable = self.error_text)
        self.enter_callback = enter_callback

    def error(self, message):
        self.error_text.set(message)
        self.error_label.pack()
    
    def success(self, user):
        self.enter_callback(user)

    def verify(self, search_result):
        if not isinstance(search_result, list):
            search_result = [search_result]
        if len(search_result) == 0:
            self.error("Usuário não encontrado")
        elif search_result[0].password != self.password.get_content():
            self.error("Senha incorreta")
        else:
            self.success(search_result[0])

    def attempt(self):
        match self.type.get_selection():
            case "Administrador": user_controller = AdministratorController()
            case "Estudante": user_controller = StudentController()
        
        search_result = user_controller.read(self.id.get_content()) 
        
        self.verify(search_result)
        
    def mainloop(self, *args, **kwargs):
        ttk.Label(self.wrapper, text = "RuConnect", 
                  font = font.Font(family = 'Helvetica', size = 26, weight = "bold")).pack(pady = 10)
        self.id.pack(in_ = self.wrapper)
        self.password.pack(in_ = self.wrapper)
        self.type.pack(in_ = self.wrapper)
        self.button.pack(in_ = self.wrapper, pady = 20)
        self.wrapper.pack(expand = True, fill = "both")
        self.container.pack(expand = True)
        super().mainloop(*args, **kwargs)
