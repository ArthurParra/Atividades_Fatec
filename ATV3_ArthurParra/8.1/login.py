from tkinter import *
from tkinter import messagebox
import subprocess
import sys

# Tela de login da versão 8.1 do sistema
class TelaLogin:
    def __init__(self):
        self.tela = Tk()
        self.tela.title("Acesso ao Sistema")
        self.largura = 400
        self.altura = 200
        self.centralizar_tela()
        self.tela.resizable(False, False)
        self.criar_componentes()
        self.tela.mainloop()

    def centralizar_tela(self):
        largura_screen = self.tela.winfo_screenwidth()
        altura_screen = self.tela.winfo_screenheight()
        posx = largura_screen/2 - self.largura/2
        posy = altura_screen/2 - self.altura/2
        # Centraliza a janela de login na tela
        self.tela.geometry("%dx%d+%d+%d" % (self.largura, self.altura, posx, posy))

    def criar_componentes(self):
        # Cria os campos de usuário e senha
        Label(self.tela, text="Usuário").place(x=50, y=60)
        Label(self.tela, text="Senha").place(x=50, y=100)
        self.txt_usuario = Entry(self.tela, width=20)
        self.txt_usuario.place(x=100, y=60)
        self.txt_senha = Entry(self.tela, width=20, show="*")
        self.txt_senha.place(x=100, y=100)
        self.carregar_icones()
        self.criar_botoes()

    def carregar_icones(self):
        # Tenta carregar imagens para ícones dos botões
        try:
            self.foto_acesso = PhotoImage(file=r"icones\acesso.png")
            self.foto_sair = PhotoImage(file=r"icones\sair.png")
        except:
            self.foto_acesso = None
            self.foto_sair = None

    def criar_botoes(self):
        # Botões de ação na tela de login
        Button(self.tela, text="Acessar", image=self.foto_acesso, compound=TOP, command=self.validar_acesso).place(x=250, y=50)
        Button(self.tela, text="Sair", image=self.foto_sair, compound=TOP, command=self.sair).place(x=320, y=50)

    def validar_acesso(self):
        # Valida se usuário e senha estão corretos
        if self.txt_usuario.get() == "admin" and self.txt_senha.get() == "123":
            self.tela.destroy()
            subprocess.run([sys.executable, "Menu.py"])
        else:
            messagebox.showerror("Erro de Login", "Usuário ou senha incorretos")

    def sair(self):
        # Fecha a janela após confirmação
        if messagebox.askquestion("Sair", "Você tem certeza?") == "yes":
            self.tela.destroy()