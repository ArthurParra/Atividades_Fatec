class Carro: 
    #construtor de classe
    def _init_(self, nome):
        self.nome = nome
        
        #método da classe carro
    def acelerar(self):
        print(self.nome , "Está acelerando...")
            
#instanciando o objeto car da classe Carro
car = Carro('fusca')
print(car.nome)
car.acelerar()

c = Carro('Uno')
print(c.nome)
c.acelerar()