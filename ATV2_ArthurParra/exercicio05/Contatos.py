from tkinter import *

class Contatos:
    def __init__(self):
        self.tela = Tk()
        self.configurar_tela()
        self.criar_componentes()
        
        #atributos privados
        self.__nome = ""
        self.__telefone = ""
        self.__cidade = ""
        self.__endereco = ""
        
    @property
    def _nome(self):
        return self.__nome
    @_nome.setter
    def _nome(self, value):
        self.__nome = value
        
    @property
    def _telefone(self):
        return self._telefone
    @_telefone.setter
    def _telefone(self, value):
        self.__telefone = value
        
    @property
    def _cidade(self):
        return self.__cidade
    @_cidade.setter
    def _cidade(self, value):
        self.__cidade = value
        
    @property
    def _endereco(self):
        return self.__endereco
    @_endereco.setter
    def _endereco(self, value):
        self.__endereco = value

      
    def configurar_tela(self):
        self.tela.title("Contatos")
        self.tela.configure(bg="#F3E5F5")
        
        largura = 800
        altura = 600
        
        largura_screen = self.tela.winfo_screenwidth()
        altura_screen = self.tela.winfo_screenheight()
        
        posx = largura_screen / 2 - largura /2
        posy = altura_screen / 2 - altura /2

        self.tela.geometry("%dx%d+%d+%d" % (largura,altura,posx,posy))
               
    def criar_componentes(self):
        self.frame = Frame(self.tela, bg="#CE93D8", padx=20, pady=20)
        self.frame.pack(expand=True)
        
        self.titulo = Label(self.frame, text="Contatos" )
        
        self.titulo.grid(row=0, column=0, columnspan=2, pady=10)
        
        #nome:
        Label(self.frame, text="Digite o nome:").grid(row=1, column=0, sticky="w", pady=5)
        self.nome = Entry(self.frame)
        self.nome.grid(row=1, column=1, pady=5)
        
        #telefone:
        Label(self.frame, text="Telefone:").grid(row=2, column=0, sticky="w", pady=5)
        self.telefone = Entry(self.frame)
        self.telefone.grid(row=2, column=1, pady=5)
        
        #cidade:
        Label(self.frame, text="Cidade:").grid(row=3, column=0, sticky="w", pady=5)
        self.cidade = Entry(self.frame)
        self.cidade.grid(row=3, column=1, pady=5)
        
        #endereco:
        Label(self.frame, text="Endereço:").grid(row=4, column=0, sticky="w", pady=5)
        self.endereco = Entry(self.frame)
        self.endereco.grid(row=4, column=1, pady=5)
 
        
        
        self.btn_salvar = Button(self.frame, text="Mostrar dados do contato: ", command=self.salvar)
        self.btn_salvar.grid(row=5, column=0, columnspan=2, pady=10)
        
    def salvar(self):
        self.__nome = self.nome.get()
        self.__telefone = self.telefone.get()
        self.__cidade = self.cidade.get()
        self.__endereco = self.endereco.get()
        
        
        self.mostrar = Label(self.frame, text="", bg="#4A148C", fg="#000000", width=30, height=6, justify="center" )
        self.mostrar.grid(row=5, column=0, columnspan=2, pady=10)
        self.mostrar.config(text=f"Nome: {self.__nome}\n Telefone: {self.__telefone}\n Cidade: {self.__cidade}\n Endereço: {self.__endereco}")
        
        
        
    def iniciar(self):
        self.tela.mainloop()