from tkinter import *

class Carro:
    def __init__(self):
        self.tela = Tk()
        self.configurar_tela()
        self.criar_componentes()

        #atibutos privados
        self.__nomeCarro = ""
        self.__distancia = 0
        self.__tempo = 0
        self.__velocidade = 0

    @property
    def _nomeCarro(self):
        return self.__nomeCarro
    @_nomeCarro.setter
    def _nomeCarro(self, value):
        self.__nomeCarro = value

    @property
    def _distancia(self):
        return self.__distancia
    @_distancia.setter
    def _distancia(self, value):
        self.__distancia = value

    @property
    def _tempo(self):
        return self.__tempo
    @_tempo.setter
    def _tempo(self, value):
        self.__tempo = value

    def configurar_tela(self):
        self.tela.title("Calculo Velocidade")
        self.tela.configure(bg="#FFF0F5")

        largura = 800
        altura = 500

        largura_screen = self.tela.winfo_screenwidth()
        altura_screen = self.tela.winfo_screenheight()

        posx = largura_screen / 2 - largura /2
        posy = altura_screen / 2 - altura /2

        self.tela.geometry("%dx%d+%d+%d" % (largura,altura,posx,posy))

    def criar_componentes(self):
        self.frame = Frame(self.tela, bg="#F8BBD9", padx=20, pady=20)
        self.frame.pack(expand=True)

        self.titulo = Label(self.frame, text="Velocidade Carro")

        self.titulo.grid(row=0, column=0, columnspan=2, pady=10)

        #nome carro:
        Label(self.frame, text="Nome Carro:").grid(row=1, column=0, sticky="w", pady=5)
        self.nome = Entry(self.frame)
        self.nome.grid(row=1, column=1, pady=5)

        #distancia:
        Label(self.frame, text="Distância Percorrida em KM:").grid(row=2, column=0, sticky="w", pady=5)
        self.distancia = Entry(self.frame)
        self.distancia.grid(row=2, column=1, pady=5)

        #tempo:
        Label(self.frame, text="Tempo em minutos:").grid(row=3, column=0, sticky="w", pady=5)
        self.tempo = Entry(self.frame)
        self.tempo.grid(row=3, column=1, pady=5)

        self.btn_calcular = Button(self.frame, text="Calcular Velocidade", command=self.calcular_vel)
        self.btn_calcular.grid(row=6, column=0, columnspan=2, pady=10)

    def calcular_vel(self):
        self.__nomeCarro = self.nome.get()
        self.__distancia = float(self.distancia.get())
        self.__tempo = float(self.tempo.get())

        #calcular velocidade em m/s
        self.__velocidade = (self.__distancia * 1000) / (self.__tempo * 60)

        self.resultado = Label(self.frame, text=f"", bg="#FFE4E1", fg="#000000", width=30, height=6, justify="center")
        self.resultado.grid(row=7, column=0, columnspan=2, pady=10)
        self.resultado.config(text=f"O Carro {self.__nomeCarro}\n Percorreu {self.__distancia} metros\n Em um tempo de {self.__tempo} segundos\n\n Velocidade: {self.__velocidade:.2f} m/s")

    def iniciar(self):
        self.tela.mainloop()

