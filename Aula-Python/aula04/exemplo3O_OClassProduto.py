class Produto:
    
    def __init__(self,nome,preco,qtd):
        self.nome = nome
        self.preco = preco
        self.qtd = qtd

    #metodo mostrar info produtos
    def mostrar(self):
        print("Nome Produto: ", self.nome)
        print("Preço Produto: R$", self.preco)
        print("Quantidade: ", self.qtd)

    #metodo calcular valor total
    def calcularTotal(self):
        val_total = self.qtd * self.preco
        print(f"O valor total é R$ {round(val_total,2)}")

#intanciando o objeto e chamar os metodos da classe
prod = Produto("abacate", 4.9,76 )
prod.mostrar()
prod.calcularTotal()
