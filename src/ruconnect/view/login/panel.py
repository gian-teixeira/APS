from control.user import AdministratorController, StudentController
from persistence.user import AdministratorPersistence, StudentPersistence
from view.entry import Entry
from view.selector import Selector
from model.user import Administrator
from tkinter import Tk, ttk, font
        
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
        self.button = ttk.Button(self, text = "Entrar", command = self.enter)
        self.error_label = ttk.Label(self.container, text = "Usuário não encontrado")
        self.enter_callback = enter_callback

    def enter(self, force = False):
        if force:
            self.enter_callback(Administrator("Euler", 1655, 271))

        match self.type.get_selection():
            case "Administrador": controller = AdministratorController(AdministratorPersistence())
            case "Estudante": controller = StudentController(StudentPersistence())
        print(self.id.get_content())
        user = controller.search(self.id.get_content())
        if len(user) == 0: 
            self.error_label.pack()
            return
        user = user[0]
        if user.password == self.password.get_content():
            self.enter_callback(user)
        
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
