from tkinter import *

class Soma_Numeros:
    def __init__(self):
        self.tela = Tk()
        self.configurar_tela()
        self.criar_componentes()

        #ATRIBUTOS PRIVADOS
        self.__n1 = 0
        self.__n2 = 0
        self.__soma = 0

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
    def _soma(self):
        return self.__soma

    @_soma.setter
    def _soma(self, value):
        self.__soma = value


    def configurar_tela(self):
        self.tela.title("Aplicação O_O")
        self.tela.configure(background="#1e3743") 
        
        #DEFINE O TAMANHO PADRAO DA SUA TELA
        largura = 800
        altura = 300

        #PEGA A LARGURA E ALTURA DA TELA DO WINDOWS
        largura_screen = self.tela.winfo_screenwidth()
        altura_screen = self.tela.winfo_screenheight()

        #DEFINE O POSICIONAMENTO CENTRALIZADO
        posx = largura_screen / 2 - largura /2
        posy = altura_screen / 2 - altura /2

        #CONSTROI A TELA DE ACORDO COM AS DIMENSÕES DA TELA DO WINDOS 
        #%D SUBTITUI CADA NÚMERO    % CONCATENA CADA VARIAVEL LARGURA, ALTURA...
        self.tela.geometry("%dx%d+%d+%d" % (largura,altura,posx,posy))  

    def criar_componentes(self):
        #CRIAR FRAME  padx pady = espaçamento padding 
        self.frame = Frame(self.tela, bg= "#34495e" , padx = 20 , pady = 20)
        #pack posiciona de acordo com a tela expand => ocupa espaço na tela ao redimensionar
        self.frame.pack(expand=True)

        #TITULO
        self.titulo = Label(self.frame , text="Soma de Números")
        #grid => cria grade  row = linha colum= coluna  columspan = espaço interno coluna
        #pady = espacamento parte de cima e de baixo de 10px
        self.titulo.grid(row=0, column = 0, columnspan= 2 , pady = 10)

        #NUMERO1

        #sticky="w"  posicionamento do texto lado esquerdo(oeste)
        Label(self.frame, text="Numero 1:").grid(row =1 , column= 0, sticky= "w" , pady= 5)

        self.txt_n1 = Entry(self.frame)
        self.txt_n1.grid(row= 1, column= 1, pady = 5)

        #NUMERO2
        Label(self.frame, text="Numero 2:").grid(row =3 , column= 0, sticky= "w" , pady= 5)

        self.txt_n2 = Entry(self.frame)
        self.txt_n2.grid(row= 3, column= 1, pady = 5)

        #RESULTADO
        Label(self.frame, text="RESULTADO: ").grid(row =4 , column= 0, sticky= "w" , pady= 5)

        self.txt_resul = Entry(self.frame)
        self.txt_resul.grid(row= 4, column= 1, pady = 5)

        #BOTAO
        self.btn_botao = Button(self.frame, text= "Calcular" ,command = self.calcular)
        self.btn_botao.grid(row = 5 , column= 0, columnspan= 2, pady = 15)
    
    def calcular(self):
        #RECEBENDO OS VALORES CAIXAS DE TEXTO E GUARDANDO ATRIBUTOS 
        self.__n1 = float(self.txt_n1.get())
        self.__n2 = float(self.txt_n2.get())
        self.__soma = self.__n1 + self.__n2

        #COLOCA O RESULTADO DA SOMA NA CAIXA DE TEXTO TXT RESUL
        self.txt_resul.insert(0,self.__soma)
    
    def executar(self):
        self.tela.mainloop()

