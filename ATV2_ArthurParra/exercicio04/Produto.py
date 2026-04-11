from tkinter import *

class Produto:
    def __init__(self):
        self.tela = Tk()
        self.configurar_tela()
        self.criar_componentes()

        #atributos privados
        self.__nomeProdu = ""
        self.__quantidade = int()
        self.__valor = float()
        self.__total = float()

    @property
    def _nomeProdu(self):
        return self.__nomeProdu
    @_nomeProdu.setter
    def _nomeProdu(self, value):
        self.__nomeProdu = value

    @property
    def _quantidade(self):
        return self.__quantidade
    @_quantidade.setter
    def _quantidade(self, value):
        self.__quantidade = value

    @property
    def _valor(self):
        return self.__valor
    @_valor.setter
    def _valor(self, value):
        self.__valor = value

    @property
    def _total(self):
        return self.__total
    @_total.setter
    def _total(self, value):
        self.__total = value

    
    def configurar_tela(self):
        self.tela.title("Calculo Produto")
        self.tela.configure(background="#C8E6C9")

        largura = 800
        altura = 500

        largura_screen = self.tela.winfo_screenwidth()
        altura_screen = self.tela.winfo_screenheight()

        posx = largura_screen / 2 - largura /2
        posy = altura_screen / 2 - altura /2

        self.tela.geometry("%dx%d+%d+%d" % (largura,altura,posx,posy))

    def criar_componentes(self):
        self.frame = Frame(self.tela, bg= "#2E8B57", padx=20, pady=20)
        self.frame.pack(expand=True)

        self.titulo = Label(self.frame, text="Calculo Total Produto")

        self.titulo.grid(row=0, column=0, columnspan=2, pady=10)

        #nome produto:
        Label(self.frame, text="Nome do Produto:").grid(row=1, column=0, sticky="w", pady=5)
        self.txt_nomeProdu = Entry(self.frame)
        self.txt_nomeProdu.grid(row=1, column=1, pady=5)

        #quantidade:
        Label(self.frame, text="Quantidade Comprada:").grid(row=2, column=0, sticky="w", pady=5)
        self.txt_quantidade = Entry(self.frame)
        self.txt_quantidade.grid(row=2, column=1, pady=5)

        #valor:
        Label(self.frame, text="Preço Produto: ").grid(row=3, column=0, sticky="w", pady=5)
        self.txt_valor = Entry(self.frame)
        self.txt_valor.grid(row=3, column=1, pady=5)

        

        self.resultado = Label(self.frame, text="", bg="#98FB98", fg="#000000", width=30, height=6, justify="center")
        self.resultado.grid(row=5, column=0, columnspan=2, pady=10)

        self.btn = Button(self.frame, text="Total", command=self.calcular)
        self.btn.grid(row=6, column=0, columnspan=2, pady=10)

    def calcular(self):
        self.__nomeProdu = self.txt_nomeProdu.get()
        self.__quantidade = int(self.txt_quantidade.get())
        self.__valor = float(self.txt_valor.get())
        self.__total = self.__quantidade * self.__valor

        #total:
        Label(self.frame, text="Total Produto: ").grid(row=4, column=0, sticky="w", pady=5)
        self.txt_total = Entry(self.frame)
        self.txt_total.grid(row=4, column=1, pady=5)

        self.resultado.config(text=f"O produto {self.__nomeProdu}\n Preço: R${self.__valor:.2f}\n Quantidade: {self.__quantidade}\n  Total: R$ {self.__total:.2f}")

    def iniciar(self):
        self.tela.mainloop()
