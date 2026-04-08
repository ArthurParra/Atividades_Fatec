from tkinter import *

class Clientes:
    def __init__(self):
        self.tela = Tk()
        self.configurar_tela()
        self.criar_componentes()
        #self.mostrar_dados()
        
        #atributos privados
        self.__nome = ""
        self.__email = ""
        self.__telefone = ""
        self.__endereco = ""

    @property
    def _nome(self):
        return self.__nome
    @_nome.setter
    def _nome(self, value):
        self.__nome = value

    @property
    def _email(self):
        return self.__email
    @_email.setter
    def _email(self, value):
        self.__email = value

    @property
    def _telefone(self):
        return self.__telefone
    @_telefone.setter
    def _telefone(self, value):
        self.__telefone = value

    @property
    def _endereco(self):
        return self.__endereco
    @_endereco.setter
    def _endereco(self, value):
        self.__endereco = value

    def configurar_tela(self):
        self.tela.title("Cadastro de Clientes")
        self.tela.configure(background="#1e3743")

        #definir tamanho padrão da tela
        largura = 800
        altura = 300

        #Pegar Alt e Lar da tela do windows
        largura_screen = self.tela.winfo_screenwidth()
        altura_screen = self.tela.winfo_screenheight()

        #definir posicionamento centralizado
        posx = largura_screen / 2 - largura / 2
        posy = altura_screen / 2 - altura / 2

        #construir a tela de acordo com as dimensoes da tela do windows
        self.tela.geometry("%dx%d+%d+%d" % (largura,altura,posx,posy))

    def criar_componentes(self):
        #criar frame
        self.frame = Frame(self.tela, bg="#34495e", padx=20, pady=20)
        self.frame.pack(expand=True)

        #titulo
        self.titulo = Label(self.frame, text="Cadastro de Clientes")
        self.titulo.grid(row=0, column=0, columnspan=2, pady=10)

        #NOME:

        Label(self.frame, text="Nome: ").grid(row=1, column=0, sticky="w", pady=5)
        self.txt_nome = Entry(self.frame)
        self.txt_nome.grid(row=1, column=1, pady=5)

        #EMAIL:

        Label(self.frame, text="Email: ").grid(row=2, column=0, sticky="w", pady=5)
        self.txt_email = Entry(self.frame)
        self.txt_email.grid(row=2, column=1, pady=5)

        #TELEFONE:

        Label(self.frame, text="Telefone: ").grid(row=3, column=0, sticky="w", pady=5)
        self.txt_telefone = Entry(self.frame)
        self.txt_telefone.grid(row=3, column=1, pady=5)

        #ENDEREÇO:

        Label(self.frame, text="Endereço: ").grid(row=4, column=0, sticky="w", pady=5)
        self.txt_endereco = Entry(self.frame)
        self.txt_endereco.grid(row=4, column=1, pady=5)

        #BOTAO CADASTRAR

        self.btn_cadastrar = Button(self.frame, text="Cadastrar Cliente", command=self.cadastrar_cliente)
        self.btn_cadastrar.grid(row=5, column=0, columnspan=2, pady=10)

    def cadastrar_cliente(self):

        self.__nome = self.txt_nome.get()
        self.__email = self.txt_email.get()
        self.__telefone = self.txt_telefone.get()
        self.__endereco = self.txt_endereco.get()
        
        self.mostrar_dados()

        #self.mostrar_dados()


    def mostrar_dados(self):
        from tkinter import messagebox
        dados = f"Nome: {self.__nome}\n Email: {self.__email}\n Telefone: {self.__telefone}\n Endereço: {self.__endereco}"
        messagebox.showinfo("Dados do Cliente", dados)

    # terminar metodo de mostrar dados na proxima aula
    

    



    def iniciar(self):
        self.tela.mainloop()



        

