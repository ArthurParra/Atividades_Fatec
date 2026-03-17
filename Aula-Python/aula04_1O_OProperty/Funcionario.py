class Funcionario:
    def __init__(self):
        self.__nome = ""
        self.__salario = 0.0
        self.__salarioAtual = 0.0
        self.__salAumento = 0.0

    def cadastrarFunc(self):
        self.__nome = input("Digite o nome do funcionario: ")
        self.__idade = int(input("Digite a idade do funcionario: "))
        self.__salario = float(input("Digite o salario do funcionario: "))
    
    def calcularAumento(self):
        self.__salarioAtual = self.__salarioAtual + (self.__salarioAtual * 10)/100
        return self.__salAumento