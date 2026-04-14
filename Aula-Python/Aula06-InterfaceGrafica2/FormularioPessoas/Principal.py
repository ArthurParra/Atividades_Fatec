from Pessoas import ControlePessoas

class Principal:
    @staticmethod
    def main():
        #instanciar classe 
        obj = ControlePessoas()
        obj.executar()

if __name__ == "__main__":
    Principal.main()