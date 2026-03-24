from tkinter import *

class Aplicacao:
    def __init__(self):
        self.tela = Tk()
        self.configurar_tela()
        self.criat_componentes()

        # atribuindo privativos
        self.__n1 = 0
        self.__n2 = 0
        self.__soma = 0

    def configurar_tela(self):
        self.tela.title("Aplicação O_O")
        # self.configure(background=)

        #continuar na proxima aula
        