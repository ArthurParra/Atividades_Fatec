import tkinter as tk
from tkinter import Menu, Label, Button, messagebox
import subprocess
import sys
import os

# Interface principal (menu) do sistema de vendas
# Garante que Pillow está instalado para manipular imagens
try:
    from PIL import Image, ImageTk
except:
    os.system(f'"{sys.executable}" -m pip install pillow')
    from PIL import Image, ImageTk

class TelaMenuSistema:
    def __init__(self):
        self.tela = tk.Tk()
        self.tela.title("SISTEMA DE VENDAS - MENU PRINCIPAL")

        # Dimensões da janela conforme o slide
        self.largura = 1000
        self.altura = 700

        self.centralizar_tela()
        self.carregar_imagem_fundo()
        self.criar_menu()
        self.carregar_icones()
        self.criar_botoes()

        self.tela.mainloop()

    # Configuração para centralizar a janela na tela do computador
    def centralizar_tela(self):
        # Centraliza a janela do menu
        largura_screen = self.tela.winfo_screenwidth()
        altura_screen = self.tela.winfo_screenheight()
        posx = largura_screen/2 - self.largura/2
        posy = altura_screen/2 - self.altura/2
        self.tela.geometry("%dx%d+%d+%d" % (self.largura, self.altura, posx, posy))
        self.tela.resizable(False, False)

    # Carrega a imagem de fundo (Página 12 do PDF)
    def carregar_imagem_fundo(self):
        # Tenta carregar uma imagem de fundo, senão usa cor sólida
        caminho = r"icones\imagem_fundo.jpg"
        if os.path.exists(caminho):
            imagem = Image.open(caminho).resize((1000, 700))
            self.imagem_fundo = ImageTk.PhotoImage(imagem)
            self.lbl_fundo = Label(self.tela, image=self.imagem_fundo)
            self.lbl_fundo.place(x=0, y=0)
        else:
            self.tela.configure(bg="lightblue")

    # Estrutura de Menus Superiores (Páginas 3 a 7 do PDF)
    def criar_menu(self):
        # Cria barra de menus superior com opções Arquivo e Gestão
        barra_menus = Menu(self.tela)
        opcoes_menus_arquivos = Menu(barra_menus)
        opçoes_menus_gestao = Menu(barra_menus)
        opcoes_novo = Menu(opcoes_menus_arquivos)

        # Menu Arquivo
        barra_menus.add_cascade(label="Arquivo", menu=opcoes_menus_arquivos)
        opcoes_menus_arquivos.add_cascade(label="Novo", menu=opcoes_novo)
        opcoes_novo.add_command(label="Cadastrar")
        opcoes_menus_arquivos.add_command(label="Abrir")
        opcoes_menus_arquivos.add_command(label="Salvar")
        opcoes_menus_arquivos.add_separator()
        opcoes_menus_arquivos.add_command(label="Sair", command=self.tela.quit)

        # Menu Gestão - Configurado para o seu sistema de vendas
        barra_menus.add_cascade(label="Gestão", menu=opçoes_menus_gestao)
        opçoes_menus_gestao.add_command(label="Produtos", command=self.abrir_produtos)
        opçoes_menus_gestao.add_command(label="Clientes", command=self.abrir_clientes)
        
        self.tela.config(menu=barra_menus)

    # Carrega os ícones dos botões (Página 11 do PDF)
    def carregar_icones(self):
        # Carrega ícones usados nos botões (retorna None se não encontrados)
        self.logo = self.carregar_png(r"icones\logo.png", 70, 70)
        self.produtos_img = self.carregar_png(r"icones\logo_animais.png", 80, 80) # Reaproveitando o ícone visual
        self.clientes_img = self.carregar_png(r"icones\logo_usuarios.png", 80, 80)
        self.servicos_img = self.carregar_png(r"icones\logo_servicos.png", 80, 80)
        self.logout_img = self.carregar_png(r"icones\logout.png", 80, 80)

    def carregar_png(self, caminho, largura, altura):
        if os.path.exists(caminho):
            return ImageTk.PhotoImage(Image.open(caminho).resize((largura, altura)))
        return None

    # Posicionamento dos botões na tela (Página 16 do PDF)
    def criar_botoes(self):
        # Botões principais do menu: produtos, clientes, serviços e logout
        Label(self.tela, text="SISTEMA VENDAS", image=self.logo, compound="top", font=("Arial", 10, "bold")).place(x=850, y=560)
        
        Button(self.tela, text="Produtos", image=self.produtos_img, compound="top", command=self.abrir_produtos, width=100).place(x=100, y=200)
        Button(self.tela, text="Clientes", image=self.clientes_img, compound="top", command=self.abrir_clientes, width=100).place(x=320, y=200)
        Button(self.tela, text="Serviços", image=self.servicos_img, compound="top", command=self.servicos_msg, width=100).place(x=540, y=200)
        Button(self.tela, text="Logout", image=self.logout_img, compound="top", command=self.logout, width=100).place(x=760, y=200)

    # Métodos de chamada utilizando subprocess (Página 14 do PDF)
    def abrir_clientes(self):
        # Abre a tela de clientes em processo separado
        subprocess.run([sys.executable, "clientes.py"])

    def abrir_produtos(self):
        # Abre a tela de produtos (arquivo produtos.py)
        subprocess.run([sys.executable, "produtos.py"])

    def logout(self):
        # Fecha o menu e volta para a tela de login
        self.tela.destroy()
        subprocess.run([sys.executable, "login.py"])

    def servicos_msg(self):
        # Mensagem de aviso que a tela de serviços ainda não foi implementada
        messagebox.showinfo("Serviços", "Tela em desenvolvimento.")

if __name__ == "__main__":
    TelaMenuSistema()   