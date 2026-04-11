from Contatos import Contatos

class Principal:
    @staticmethod
    def main():
        contatos = Contatos()
        contatos.iniciar()
        
if __name__ == "__main__":
    Principal.main()