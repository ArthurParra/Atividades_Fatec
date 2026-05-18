from tkinter import *
from tkinter import ttk, messagebox

class GestaoProdutos:
    def __init__(self):
        self.tela = Tk()
        self.tela.title("Gestão de Produtos")
        self.largura = 700
        self.altura = 400
        
        self.centralizar_tela()
        self.criar_componentes()
        self.tela.mainloop()

    def centralizar_tela(self):
        largura_screen = self.tela.winfo_screenwidth()
        altura_screen = self.tela.winfo_screenheight()
        posx = largura_screen/2 - self.largura/2
        posy = altura_screen/2 - self.altura/2
        self.tela.geometry("%dx%d+%d+%d" % (self.largura, self.altura, posx, posy))
        self.tela.resizable(False, False)

    def criar_componentes(self):
        # LABELS (Baseado nos atributos do Diagrama UML)
        Label(self.tela, text="Cadastro de Produtos", font=("Arial", 18, "bold")).place(x=220, y=20)
        Label(self.tela, text="Código (int):").place(x=100, y=90)
        Label(self.tela, text="Nome Produto (String):").place(x=100, y=130)
        Label(self.tela, text="Quantidade (int):").place(x=100, y=170)
        Label(self.tela, text="Preço (double):").place(x=100, y=210)
        Label(self.tela, text="Total (double):").place(x=100, y=250)

        # CAMPOS DE ENTRADA
        self.txt_codigo = Entry(self.tela, width=15)
        self.txt_nome = Entry(self.tela, width=45)
        self.txt_quantidade = Entry(self.tela, width=15)
        self.txt_preco = Entry(self.tela, width=15)
        
        # Campo de total fica desabilitado para o usuário não alterar o cálculo
        self.txt_total = Entry(self.tela, width=15, state="disabled")

        self.txt_codigo.place(x=260, y=90)
        self.txt_nome.place(x=260, y=130)
        self.txt_quantidade.place(x=260, y=170)
        self.txt_preco.place(x=260, y=210)
        self.txt_total.place(x=260, y=250)

        self.criar_botoes()

    def criar_botoes(self):
        try:
            self.foto_salvar = PhotoImage(file=r"icones\salvar.png")
            self.foto_consultar = PhotoImage(file=r"icones\consultar.png")
            self.foto_sair = PhotoImage(file=r"icones\sair.png")
        except:
            self.foto_salvar = self.foto_consultar = self.foto_sair = None

        Button(self.tela, text="Calcular Total", command=self.calcular_total_venda).place(x=400, y=208)

        self.btn_salvar = Button(self.tela, text="Cadastrar", image=self.foto_salvar, compound=TOP, command=self.cadastrar_produto, width=80)
        self.btn_consultar = Button(self.tela, text="Consultar", image=self.foto_consultar, compound=TOP, command=self.consultar_produto, width=80)
        self.btn_sair = Button(self.tela, text="Sair", image=self.foto_sair, compound=RIGHT, command=self.tela.destroy)

        self.btn_salvar.place(x=180, y=310)
        self.btn_consultar.place(x=300, y=310)
        self.btn_sair.place(x=580, y=340)

    # REQUISITOS DO DIAGRAMA UML (+cadastrarProduto e +consultarProduto)
    def calcular_total_venda(self):
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
            messagebox.showerror("Erro", "Insira valores numéricos válidos em Quantidade e Preço.")
            return 0

    def cadastrar_produto(self):
        self.calcular_total_venda()
        nome = self.txt_nome.get()
        if nome:
            messagebox.showinfo("Sucesso", f"Produto '{nome}' cadastrado com sucesso! (void)")
        else:
            messagebox.showwarning("Aviso", "Preencha o nome do produto.")

    def consultar_produto(self):
        codigo = self.txt_codigo.get()
        if codigo:
            messagebox.showinfo("Consulta", f"Buscando produto do código {codigo}... Consulta realizada!")
        else:
            messagebox.showwarning("Aviso", "Digite um código para consultar.")

if __name__ == "__main__":
    GestaoProdutos()