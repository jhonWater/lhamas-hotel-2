import tkinter as tk
from app.screens.LoginUser import Login
from app.screens.CadastroScreen import Cadastrar
from app.screens.FuncionarioScreen import FuncionarioScreen
from app.screens.ClientesScreen import Clientes
from app.screens.QuartosScreen import Quartos
from app.screens.AdminScreen import AdminScreen
from app.screens.CadastraFuncio import CadastraFuncio
from app.database.FuncionarioRepo import FuncionarioRepo
from app.database.AdminRepo import AdminDB
from tkinter import messagebox


class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title('Lhamas Hotel')
        self.geometry('700x400')
        self.session= None
        self.show_login()

    def show_funcionarioscreen(self):
    	self.funciotela = FuncionarioScreen(self)
    	self.funciotela.pack()

    def show_adminscreen(self):
        self.adm = AdminScreen(self)
        self.adm.pack()

    def show_login(self):
        self.login = Login(self)
        self.login.pack()
    
    def show_cadastrar(self):
        self.cadastrar = Cadastrar(self)
        self.cadastrar.pack()

    def show_cadastrafuncionario(self):
        self.cadastrafuncio = CadastraFuncio(self)
        self.cadastrafuncio.pack()
    
    def show_clientes(self):
        self.clientes = Clientes(self)
        self.clientes.pack()
    
    def show_quartos(self):
        self.quartos=Quartos(self)
        self.quartos.pack()
        
    def clear_campo(self):
        self.cadastrar =Cadastrar(self)
        self.cadastrar.pack()
        
    def clear_campoF(self):
        self.cadastrafuncio = CadastraFuncio(self)
        self.cadastrafuncio.pack()

    def add_funcio(self):
        self.add_funcio = FuncionarioRepo()

    def loginAdmin(self, cpf,senha):
        self.cpfa= cpf
        self.senhab = senha
        try:
            if AdminDB.check_admin(self.cpfa,self.senhab) == True:
                return True
        except Exception:
            messagebox.showerror('Error', 'Ih... não funfou, hein')
root = App()
root.mainloop()