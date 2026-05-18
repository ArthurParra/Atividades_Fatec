from tkinter import *
from tkinter import messagebox
import sys
import os

# Tela para cadastro e consulta de clientes usando MongoDB
try:
    import pymongo
except:
    os.system(f'"{sys.executable}" -m pip install pymongo')
    import pymongo

class CadastroClientes:
    def __init__(self):
        self.tela = Tk()
        self.tela.title("Cadastro de Clientes - Sistema de Vendas")
        self.tela.configure(bg="#ffffff")
        self.largura = 600
        self.altura = 350
        
        self.centralizar_tela()
        self.conectar_banco()
        self.criar_componentes()
        self.tela.mainloop()

    def centralizar_tela(self):
        # Centraliza a janela de cadastro de clientes
        largura_screen = self.tela.winfo_screenwidth()
        altura_screen = self.tela.winfo_screenheight()
        posx = int(largura_screen / 2 - self.largura / 2)
        posy = int(altura_screen / 2 - self.altura / 2)
        self.tela.geometry(f"{self.largura}x{self.altura}+{posx}+{posy}")
        self.tela.resizable(False, False)

    def conectar_banco(self):
        # Tenta conectar ao MongoDB local e preparar a coleção 'clientes'
        try:
            self.cliente_mongo = pymongo.MongoClient("mongodb://localhost:27017/")
            self.db = self.cliente_mongo["sistema_vendas"]
            self.collection = self.db["clientes"]
        except Exception as e:
            messagebox.showerror("Erro de Conexão", f"Não foi possível conectar ao MongoDB: {e}")

    def criar_componentes(self):
        # Cria rótulos e campos conforme o diagrama de classes
        Label(self.tela, text="Controle de Clientes (UML)", font=("Arial", 16, "bold"), bg="#ffffff", fg="#333333").place(x=50, y=20)

        # Labels do Diagrama de Classes
        Label(self.tela, text="Código (int):", bg="#ffffff").place(x=50, y=80)
        Label(self.tela, text="Nome Cliente (string):", bg="#ffffff").place(x=50, y=120)
        Label(self.tela, text="CPF (string):", bg="#ffffff").place(x=50, y=160)
        Label(self.tela, text="Telefone (string):", bg="#ffffff").place(x=50, y=200)
        Label(self.tela, text="Endereço (string):", bg="#ffffff").place(x=50, y=240)

        # Campos de entrada
        self.txt_codigo = Entry(self.tela, width=15, bg="#f0f0f0")
        self.txt_nome = Entry(self.tela, width=40, bg="#f0f0f0")
        self.txt_cpf = Entry(self.tela, width=20, bg="#f0f0f0")
        self.txt_telefone = Entry(self.tela, width=20, bg="#f0f0f0")
        self.txt_endereco = Entry(self.tela, width=40, bg="#f0f0f0")

        self.txt_codigo.place(x=200, y=80)
        self.txt_nome.place(x=200, y=120)
        self.txt_cpf.place(x=200, y=160)
        self.txt_telefone.place(x=200, y=200)
        self.txt_endereco.place(x=200, y=240)

        # Botões de ação: cadastrar e mostrar cliente
        Button(self.tela, text="Cadastrar Cliente", command=self.cadastrarCliente, bg="#4CAF50", fg="white", width=15).place(x=150, y=290)
        Button(self.tela, text="Mostrar Cliente", command=self.mostrarCliente, bg="#2196F3", fg="white", width=15).place(x=300, y=290)

    def dados(self):
        # Retorna dicionário com dados do cliente para o MongoDB
        return {
            "_id": self.txt_codigo.get(),  # Usa o código como chave primária no Mongo
            "nomeCliente": self.txt_nome.get(),
            "cpf": self.txt_cpf.get(),
            "telefone": self.txt_telefone.get(),
            "endereco": self.txt_endereco.get()
        }

    def limpar(self):
        # Limpa os campos de entrada
        self.txt_codigo.delete(0, END)
        self.txt_nome.delete(0, END)
        self.txt_cpf.delete(0, END)
        self.txt_telefone.delete(0, END)
        self.txt_endereco.delete(0, END)

    # + cadastrarCliente(): void
    def cadastrarCliente(self):
        # Insere cliente no MongoDB após validações básicas
        if not self.txt_codigo.get() or not self.txt_nome.get():
            messagebox.showwarning("Aviso", "Código e Nome são obrigatórios!")
            return
        try:
            self.collection.insert_one(self.dados())
            messagebox.showinfo("Sucesso", "Cliente cadastrado com sucesso no MongoDB! (void)")
            self.limpar()
        except pymongo.errors.DuplicateKeyError:
            messagebox.showerror("Erro", "Já existe un cliente com este código!")

    # + mostrarCliente(): void
    def mostrarCliente(self):
        # Busca e exibe dados do cliente pelo código
        codigo = self.txt_codigo.get()
        if not codigo:
            messagebox.showwarning("Aviso", "Digite o código para buscar.")
            return
        
        resultado = self.collection.find_one({"_id": codigo})
        if resultado:
            self.limpar()
            self.txt_codigo.insert(0, resultado["_id"])
            self.txt_nome.insert(0, resultado["nomeCliente"])
            self.txt_cpf.insert(0, resultado["cpf"])
            self.txt_telefone.insert(0, resultado["telefone"])
            self.txt_endereco.insert(0, resultado["endereco"])
            messagebox.showinfo("Sucesso", "Dados do cliente carregados! (void)")
        else:
            messagebox.showerror("Erro", "Cliente não encontrado.")

if __name__ == "__main__":
    CadastroClientes()