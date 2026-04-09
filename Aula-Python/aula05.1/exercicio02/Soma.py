from tkinter import *

class Soma:
    def __init__(self):
        self.tela = Tk()
        self.configura_tela()
        self.criar_componentes()

        #atributos privados
        self.__num1 = 0
        self.__num2 = 0
        self.__soma = 0
        
    @property
    def _num1(self):
        return self.__num1
    @_num1.setter
    def _num1(self, value):
        self.__num1 = value
        
    @property
    def _num2(self):
        return self.__num2
    @_num2.setter
    def _num2(self, value):
        self.__num2 = value
        
    @property
    def _soma(self):
        return self.__soma
    @_soma.setter
    def _soma(self, value):
        self.__soma = value
        
    def configura_tela(self):
        self.tela.title("Soma de dois números")
        self.tela.configure(background="#F0F8FF")

        #definindo tamanho padrão da tela
        largura = 800
        altura = 300

        largura_screen = self.tela.winfo_screenwidth()
        altura_screen = self.tela.winfo_screenheight()

        posx = largura_screen / 2 - largura / 2
        posy = altura_screen / 2 - altura / 2

        self.tela.geometry("%dx%d+%d+%d" % (largura,altura,posx,posy))

    def criar_componentes(self):
        self.frame = Frame(self.tela, background="#F0F8FF", padx=20, pady=20)
        self.frame.pack(expand=True)

        #titulo
        self.titulo = Label(self.frame, text="Calculo Soma")
        self.titulo.grid(row=0, column=0, columnspan=2, pady=10)


        #num1:
        Label(self.frame, text="Digite um numero: ").grid(row=1, column=0, sticky="w", pady=5)
        self.txt_num1 = Entry(self.frame)
        self.txt_num1.grid(row=1, column=1, pady=5)

        #num2:

        Label(self.frame, text="Digite o segundo numero: ").grid(row=2, column=0, sticky="w", pady=5)
        self.txt_num2 = Entry(self.frame)
        self.txt_num2.grid(row=2, column=1, pady=5)

        #botão calcular
        self.btn_calcular = Button(self.frame, text="Calcular", command=self.calcula)
        self.btn_calcular.grid(row=3, column=0, columnspan=2, pady=10)

    def calcula(self):
        try:
            self.__num1 = float(self.txt_num1.get())
            self.__num2 = float(self.txt_num2.get())
        except ValueError:
            self.__num1 = 0
            self.__num2 = 0

        self.__soma = self.__num1 + self.__num2

        if not hasattr(self, 'txt_soma'):
            Label(self.frame, text="Resultado: ").grid(row=4, column=0, sticky="w", pady=5)
            self.txt_soma = Entry(self.frame)
            self.txt_soma.grid(row=4, column=1, pady=5)

        self.txt_soma.delete(0, END)
        self.txt_soma.insert(0, str(self.__soma))


        
        #commitar e terminar na faculdade

    def iniciar(self):
        self.tela.mainloop()