from tkinter import *
from tkinter import messagebox
import sys
import os

# Interface de produtos com operações CRUD usando MongoDB (comentários curtos)
# Garante que o PyMongo está pronto para uso
try:
    import pymongo
except:
    os.system(f'"{sys.executable}" -m pip install pymongo')
    import pymongo

class GestaoProdutos:
    def __init__(self):
        self.tela = Tk()
        self.tela.title("Controle de Produtos - CRUD MongoDB")
        self.largura = 700
        self.altura = 420
        
        self.centralizar_tela()
        self.conectar_banco()
        self.criar_componentes()
        self.tela.mainloop()

    def centralizar_tela(self):
        # Centraliza janela principal
        largura_screen = self.tela.winfo_screenwidth()
        altura_screen = self.tela.winfo_screenheight()
        posx = largura_screen/2 - self.largura/2
        posy = altura_screen/2 - self.altura/2
        self.tela.geometry("%dx%d+%d+%d" % (self.largura, self.altura, posx, posy))
        self.tela.resizable(False, False)

    def conectar_banco(self):
        # Tenta estabelecer conexão com MongoDB local
        try:
            self.cliente_mongo = pymongo.MongoClient("mongodb://localhost:27017/")
            self.db = self.cliente_mongo["sistema_vendas"]
            self.collection = self.db["produtos"]
        except Exception as e:
            messagebox.showerror("Erro de Banco", f"Falha ao conectar ao MongoDB: {e}")

    def criar_componentes(self):
        # Cria campos e rótulos para cadastro de produto
        # Título principal estilizado
        Label(self.tela, text="Cadastro de Produtos (UML + MongoDB)", font=("Arial", 16, "bold")).place(x=50, y=20)
        
        # Labels baseadas estritamente no diagrama de classes do professor
        Label(self.tela, text="Código (int):").place(x=50, y=80)
        Label(self.tela, text="Nome Produto (String):").place(x=50, y=120)
        Label(self.tela, text="Quantidade (int):").place(x=50, y=160)
        Label(self.tela, text="Preço (double):").place(x=50, y=200)
        Label(self.tela, text="Total (double):").place(x=50, y=240)

        # Campos de entrada de dados
        self.txt_codigo = Entry(self.tela, width=15, bg="#fcfcfc")
        self.txt_nome_produto = Entry(self.tela, width=45, bg="#fcfcfc")
        self.txt_quantidade = Entry(self.tela, width=15, bg="#fcfcfc")
        self.txt_preco = Entry(self.tela, width=15, bg="#fcfcfc")
        self.txt_total = Entry(self.tela, width=15, state="disabled", bg="#e8e8e8") # Desabilitado para cálculo automático

        self.txt_codigo.place(x=220, y=80)
        self.txt_nome_produto.place(x=220, y=120)
        self.txt_quantidade.place(x=220, y=160)
        self.txt_preco.place(x=220, y=200)
        self.txt_total.place(x=220, y=240)

        # Botão para calcular total antes de salvar
        Button(self.tela, text="Calcular Total", command=self.atualizar_calculo_total).place(x=340, y=196)

        self.carregar_botoes_crud()

    def carregar_botoes_crud(self):
        # Carrega ícones dos botões, ou usa texto se não encontrar as imagens
        # Tentativa de carregar as imagens da sua pasta 'icones'
        try:
            self.icon_salvar = PhotoImage(file=r"icones\salvar.png")
            self.icon_alterar = PhotoImage(file=r"icones\alterar.png")
            self.icon_excluir = PhotoImage(file=r"icones\excluir.png")
            self.icon_consultar = PhotoImage(file=r"icones\consultar.png")
            self.icon_sair = PhotoImage(file=r"icones\sair.png")
        except:
            # Caso os caminhos falhem, os botões exibirão apenas texto sem quebrar o código
            self.icon_salvar = self.icon_alterar = self.icon_excluir = self.icon_consultar = self.icon_sair = None

        # Botões de ação: cadastrar, alterar, excluir, consultar e sair
        # Botões de Ação com Ícones posicionados de forma limpa na parte inferior
        Button(self.tela, text="Cadastrar", image=self.icon_salvar, compound=TOP, command=self.cadastrarProduto, width=85).place(x=80, y=300)
        Button(self.tela, text="Alterar", image=self.icon_alterar, compound=TOP, command=self.alterarProduto, width=85).place(x=190, y=300)
        Button(self.tela, text="Excluir", image=self.icon_excluir, compound=TOP, command=self.excluirProduto, width=85).place(x=300, y=300)
        Button(self.tela, text="Consultar", image=self.icon_consultar, compound=TOP, command=self.consultarProduto, width=85).place(x=410, y=300)
        
        Button(self.tela, text="Sair", image=self.icon_sair, compound=RIGHT, command=self.tela.destroy).place(x=590, y=350)

    # Função utilitária para capturar e estruturar o dicionário para o MongoDB
    def obter_estrutura_dados(self):
        # Retorna dicionário pronto para inserir/atualizar no MongoDB
        total_calculado = self.atualizar_calculo_total()
        if total_calculado is None:
            return None
            
        return {
            "_id": self.txt_codigo.get(), # Código como chave primária única
            "nomeProduto": self.txt_nome_produto.get(),
            "quantidade": int(self.txt_quantidade.get()),
            "preco": float(self.txt_preco.get()),
            "total": float(total_calculado)
        }

    def limpar_campos(self):
        # Limpa todos os campos do formulário
        self.txt_codigo.delete(0, END)
        self.txt_nome_produto.delete(0, END)
        self.txt_quantidade.delete(0, END)
        self.txt_preco.delete(0, END)
        self.txt_total.configure(state="normal")
        self.txt_total.delete(0, END)
        self.txt_total.configure(state="disabled")

    def atualizar_calculo_total(self):
        # Calcula e atualiza o campo "total" com quantidade * preço
        try:
            qtd = int(self.txt_quantidade.get())
            preco = float(self.txt_preco.get())
            total = qtd * preco
            
            self.txt_total.configure(state="normal")
            self.txt_total.delete(0, END)
            self.txt_total.insert(0, f"{total:.2f}")
            self.txt_total.configure(state="disabled")
            return total
        except ValueError:
            return None

    # =========================================================================
    # OPERAÇÕES DO CRUD EXIGIDAS NAS AULAS 8.1 E 10.1
    # =========================================================================

    # + cadastrarProduto(): void
    def cadastrarProduto(self):
        # Insere novo produto no MongoDB após validação simples
        documento = self.obter_estrutura_dados()
        if not self.txt_codigo.get() or not self.txt_nome_produto.get():
            messagebox.showwarning("Aviso", "Código e Nome do Produto são obrigatórios!")
            return
        if documento is None:
            messagebox.showerror("Erro", "Verifique se Quantidade é número inteiro e Preço é decimal.")
            return
            
        try:
            self.collection.insert_one(documento)
            messagebox.showinfo("Sucesso", "Produto cadastrado com sucesso no MongoDB!")
            self.limpar_campos()
        except pymongo.errors.DuplicateKeyError:
            messagebox.showerror("Erro", "Já existe um produto com este código!")

    # + consultarProduto(): void
    def consultarProduto(self):
        # Busca produto por código e preenche campos da interface
        codigo = self.txt_codigo.get()
        if not codigo:
            messagebox.showwarning("Aviso", "Insira o Código para realizar a busca.")
            return
            
        resultado = self.collection.find_one({"_id": codigo})
        if resultado:
            self.limpar_campos()
            self.txt_codigo.insert(0, resultado["_id"])
            self.txt_nome_produto.insert(0, resultado["nomeProduto"])
            self.txt_quantidade.insert(0, str(resultado["quantidade"]))
            self.txt_preco.insert(0, f"{resultado['preco']:.2f}")
            self.atualizar_calculo_total()
            messagebox.showinfo("Sucesso", "Produto localizado!")
        else:
            messagebox.showerror("Não Encontrado", "Nenhum produto correspondente a este código.")

    # + alterarProduto(): void (Aula 8.1)
    def alterarProduto(self):
        # Atualiza documento existente no MongoDB
        codigo = self.txt_codigo.get()
        documento = self.obter_estrutura_dados()
        
        if not codigo or documento is None:
            messagebox.showwarning("Aviso", "Preencha os dados corretamente antes de alterar.")
            return
            
        resultado = self.collection.update_one({"_id": codigo}, {"$set": documento})
        if resultado.matched_count > 0:
            messagebox.showinfo("Sucesso", "Dados do produto atualizados com sucesso!")
            self.limpar_campos()
        else:
            messagebox.showerror("Erro", "Produto não encontrado para alteração.")

    # + excluirProduto(): void (Aula 8.1)
    def excluirProduto(self):
        # Exclui produto do MongoDB após confirmação
        codigo = self.txt_codigo.get()
        if not codigo:
            messagebox.showwarning("Aviso", "Digite o código do produto que deseja excluir.")
            return
            
        if messagebox.askyesno("Confirmar Exclusão", f"Deseja realmente apagar o produto de código {codigo}?"):
            resultado = self.collection.delete_one({"_id": codigo})
            if resultado.deleted_count > 0:
                messagebox.showinfo("Sucesso", "Produto deletado do banco de dados!")
                self.limpar_campos()
            else:
                messagebox.showerror("Erro", "Produto não encontrado.")

if __name__ == "__main__":
    GestaoProdutos()