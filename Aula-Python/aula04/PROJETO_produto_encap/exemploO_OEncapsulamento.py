class Produto:
    def __init__(self):
        self.nome = ""
        self.preco = 0.0
        self.qtd = 0

    #ENCAPSULAMENTO
    #getter nome
    def get_nome(self):
        return self.__nome
    #setter nome
    def set_nome(self, nome):
        self.__nome = nome
    
    def get_preco(self):
        return self.__preco
    def set_preco(self, preco):
        self.__preco = preco

    def get_qtd(self):
        return self.__qtd
    def set_qtd(self, qtd):
        self.__qtd = qtd


    #metodo cadastrar
    def cadastrar(self):
        print("\n === Cadastro de Produtos === \n")
        self.set_nome(input("Nome do produto: "))
        self.set_qtd(int(input("Quantidade: ")))
        self.set_preco(float(input("Valor do produto: ")))

    #método mostrar
    def mostrar(self):
        print("\n === Informações do Produto === \n")
        print("Nome do produto: ", self.get_nome())
        print("Quantidade: ", self.get_qtd())
        print("Valor do produto: R$", self.get_preco())

    #metodo calcular
    def calcular(self):
        return self.__qtd * self.__preco
    
    