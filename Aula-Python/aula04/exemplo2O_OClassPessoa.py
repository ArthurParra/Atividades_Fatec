class Pessoa:
    def __init__(self, nome, ano_nascimento):
        self.nome = nome
        self.ano_nascimento = ano_nascimento
        
        #metodo calcular idade
    def calculaIdade(self):
        anoatual = int(input("Digite o ano atual: "))
        return anoatual - self.ano_nascimento
        
#instanciar um objeto da classe Pessoa

p = Pessoa('Luiz', 2001)
pe = Pessoa('Maria', 1970)
print(p.calculaIdade())
print(f"Você {pe.nome} nasceu {pe.calculaIdade()}")
#print("Você ", pe.nome, " nasceu em ", pe.calculaIdade())

