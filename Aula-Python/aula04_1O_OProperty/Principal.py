from Funcionario import Funcionario

class Principal:
    @staticmethod
    def main():
        func = Funcionario()

        func.cadastrarFunc()
        print("O aumento é R$ ", func.calcularAumento())

if __name__ == "__main__":
    Principal.main()