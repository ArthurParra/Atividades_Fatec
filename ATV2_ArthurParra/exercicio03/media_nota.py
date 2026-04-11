from tkinter import *

class Media:
    def __init__(self):
        self.tela = Tk()
        self.configura_tela()
        self.criar_componentes()
        
        #atributos privados
        self.__n1 = 0
        self.__n2 = 0
        self.__n3 = 0
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
    def _n3(self):
        return self.__n3
    @_n3.setter
    def _n3(self, value):
        self.__n3 = value
        
    @property
    def _media(self):
        return self.__media
    @_media.setter
    def _media(self, value):
        self.__media = value
        
    def configura_tela(self):
        self.tela.title("Calculo Media")
        self.tela.configure(background="#E6F3FF")
        
        largura = 800
        altura = 600
        
        largura_screen = self.tela.winfo_screenwidth()
        altura_screen = self.tela.winfo_screenheight()
        
        posx = largura_screen / 2 - largura /2
        posy = altura_screen / 2 - altura /2
        
        self.tela.geometry("%dx%d+%d+%d" % (largura,altura,posx,posy))
        
    def criar_componentes(self):
        self.frame = Frame(self.tela, background="#B3D9FF", padx=20, pady=20)
        self.frame.pack(expand=True)
        
        self.titulo = Label(self.frame, text="Calculo Media")
        self.titulo.grid(row=0, column = 0, columnspan= 2 , pady = 10)
        
        #1º nota:
        Label(self.frame, text="Digite a primeira nota:").grid(row =1 , column= 0, sticky= "w" , pady= 5)
        self.txt_n1 = Entry(self.frame)
        self.txt_n1.grid(row=1, column=1, pady=5)
        
        #2º nota:
        Label(self.frame, text="Digite a segunda nota:").grid(row =2 , column= 0, sticky= "w" , pady= 5)
        self.txt_n2 = Entry(self.frame)
        self.txt_n2.grid(row=2, column=1, pady=5)
        
        #3º nota:
        Label(self.frame, text="Digite a terceira nota:").grid(row =3 , column= 0, sticky= "w" , pady= 5)
        self.txt_n3 = Entry(self.frame)
        self.txt_n3.grid(row=3, column=1, pady=5)
        
        #resultado:
        self.resul = Label(self.frame, text="", bg="#00AEEF", width=30, height=6, justify="center")
        self.resul.grid(row=4, column=0, columnspan=2, pady=10)
        
        #botão calcular
        self.btn_botao = Button(self.frame, text="Calcular Média", command=self.calcular)
        self.btn_botao.grid(row=5, column=0, columnspan=2, pady=15)
        
    def calcular(self):
        #recebe os valores digitados e converte para float
        self._n1 = float(self.txt_n1.get())
        self._n2 = float(self.txt_n2.get())
        self._n3 = float(self.txt_n3.get())
        self._media = (self._n1 + self._n2 + self._n3) / 3
        
        self.resul.config(text=f"Resultado Média: {self.__media:.2f}\n Aluno: {self._media:.2f}")
        
        if self._media >= 7:
            self.txt_resul.insert(15, " - Aprovado")
        elif self._media >= 3:
            self.txt_resul.insert(15, " - Exame")
        else:
            self.txt_resul.insert(15, " - Reprovado")
        
    def iniciar(self):
        self.tela.mainloop()
        
    
        