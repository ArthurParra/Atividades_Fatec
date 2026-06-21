from tkinter import *

class Calculadora:
    def __init__(self):
        self.tela = Tk()
        self.configurar_tela()
        self.criar_componentes()
        
        # definindo variaveis
        self.__n1 = 0
        self.__n2 = 0
        self.__media = 0
        
    @property
    def _n1(self):
        return self.__n1
    @_n1.setter
    def _n1(self, value):
        self.__n1 = value
        
    @property
    def _n2(self):
        return self.__n2
    @_n2.setter
    def _n2(self, value):
        self.__n2 = value
        
    @property
    def _media(self):
        return self.__media
    @_media.setter
    def _media(self, value):
        self.__media = value
        
    def configurar_tela(self):
            self.tela.title("Calculadora de Média combustivel")
            self.tela.geometry("500x400")
            self.tela.configure(bg="#6A0DAD")
            
    def criar_componentes(self):
        self.lbl1 = Label(self.tela, text="Digite a distancia percorrida (km):", bg="#00BFFF", font="Arial 12")
        self.lbl1.place(x=20, y=20)
        
        self.txt1 = Entry(self.tela, width=20)
        self.txt1.place(x=20, y=50)
        
        self.lbl2 = Label(self.tela, text="Digite a quantidade de combustivel gasta (L):", bg="#00BFFF", font="Arial 12")
        self.lbl2.place(x=20, y=90)
        
        self.txt2 = Entry(self.tela, width=20)
        self.txt2.place(x=20, y=130)
        
        self.btn = Button(self.tela, text="Calcular", command=self.calcular_media, bg="#F5F5F5", font="Arial 12")
        self.btn.place(x=20, y=160)
        
    def calcular_media(self):
        self.__n1 = float(self.txt1.get())
        self.__n2 = float(self.txt2.get())
        
        self.__media = self.__n1 / self.__n2
        
        self.exibir_resultado()
    def exibir_resultado(self):
        self.resultado = Label(self.tela, text=f"A media de consumo é: {self.__media:.2f} km/L", bg="#1A1A40", font="Arial 12", fg="#ffffff")
        self.resultado.place(x=20, y=200)
        
    def executar(self):
        self.tela.mainloop()
        
    
    