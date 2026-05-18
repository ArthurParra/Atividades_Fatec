import tkinter as tk
from tkinter import Menu, Label, Button, messagebox
import subprocess
import sys
import os
from PIL import Image, ImageTk

class TelaMenuSistema:
    def __init__(self):
        self.tela = tk.Tk()
        self.tela.title("SISTEMA DE VENDAS - MENU")
        self.largura = 1000
        self.altura = 700
        self.centralizar_tela()
        self.carregar_imagem_fundo()
        self.criar_menu()
        self.carregar_icones()
        self.criar_botoes()
        self.tela.mainloop()

    def centralizar_tela(self):
        largura_screen = self.tela.winfo_screenwidth()
        altura_screen = self.tela.winfo_screenheight()
        posx = largura_screen/2 - self.largura/2
        posy = altura_screen/2 - self.altura/2
        self.tela.geometry("%dx%d+%d+%d" % (self.largura, self.altura, posx, posy))
        self.tela.resizable(False, False)

    def carregar_imagem_fundo(self):
        caminho = r"icones\imagem_fundo.jpg"
        if os.path.exists(caminho):
            imagem = Image.open(caminho).resize((1000, 700))
            self.imagem_fundo = ImageTk.PhotoImage(imagem)
            Label(self.tela, image=self.imagem_fundo).place(x=0, y=0)
        else:
            self.tela.configure(bg="lightblue")

    def criar_menu(self):
        barra_menus = Menu(self.tela)
        opcoes_menus_arquivos = Menu(barra_menus)
        opçoes_menus_gestao = Menu(barra_menus)
        
        barra_menus.add_cascade(label="Arquivo", menu=opcoes_menus_arquivos)
        opcoes_menus_arquivos.add_command(label="Sair", command=self.tela.quit)

        barra_menus.add_cascade(label="Gestão", menu=opçoes_menus_gestao)
        opçoes_menus_gestao.add_command(label="Produtos", command=self.abrir_produtos)
        opçoes_menus_gestao.add_command(label="Clientes", command=self.abrir_clientes)
        self.tela.config(menu=barra_menus)

    def carregar_icones(self):
        self.logo = self.carregar_png(r"icones\logo.png", 70, 70)
        self.produtos_img = self.carregar_png(r"icones\logo_animais.png", 80, 80) # Reutilizando o ícone
        self.clientes_img = self.carregar_png(r"icones\logo_usuarios.png", 80, 80)
        self.logout_img = self.carregar_png(r"icones\logout.png", 80, 80)

    def carregar_png(self, caminho, largura, altura):
        if os.path.exists(caminho):
            return ImageTk.PhotoImage(Image.open(caminho).resize((largura, altura)))
        return None

    def criar_botoes(self):
        Label(self.tela, text="SISTEMA VENDAS", image=self.logo, compound="top", font=("Arial", 10, "bold")).place(x=850, y=560)
        Button(self.tela, text="Produtos", image=self.produtos_img, compound="top", command=self.abrir_produtos, width=100).place(x=200, y=200)
        Button(self.tela, text="Clientes", image=self.clientes_img, compound="top", command=self.abrir_clientes, width=100).place(x=400, y=200)
        Button(self.tela, text="Logout", image=self.logout_img, compound="top", command=self.logout, width=100).place(x=600, y=200)

    def abrir_clientes(self):
        subprocess.run([sys.executable, "clientes.py"])

    def abrir_produtos(self):
        subprocess.run([sys.executable, "produtos.py"])

    def logout(self):
        self.tela.destroy()
        subprocess.run([sys.executable, "login.py"])

if __name__ == "__main__":
    TelaMenuSistema()