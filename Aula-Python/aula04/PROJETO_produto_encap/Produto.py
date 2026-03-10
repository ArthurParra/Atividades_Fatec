#importar clase Produto
from Produto import Produto

class Principal:
    @staticmethod
    def main():
        #instanciando classe produto
        prod = Produto()
        #chamar os metodos
        prod.cadastrar()
        prod.mostrar()
        print(f"Valor total = {prod.calcular()}")

#define a inicialização pela classe principal
if __name__ == "main":
    Principal.main()