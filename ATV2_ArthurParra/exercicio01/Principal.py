from Clientes import Clientes

class Principal:
    @staticmethod
    def main():
        #instanciar classe Clientes
        cli = Clientes()
        cli.iniciar()
        

if __name__ == "__main__":
    Principal.main()