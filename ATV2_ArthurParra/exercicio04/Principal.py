from Produto import Produto

class Principal:
    @staticmethod
    def main():
        produto = Produto()
        produto.iniciar()

if __name__ == "__main__":
    Principal.main()