from Calculadora import Calculadora

class Principal:
    @staticmethod
    def main():
        calculadora = Calculadora()
        calculadora.executar()
        
if __name__ == "__main__":
    Principal.main()