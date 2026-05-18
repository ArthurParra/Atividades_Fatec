from login import TelaLogin

class Principal:
    @staticmethod
    def main():
        # Instanciar a classe já inicia o loop da tela de login
        TelaLogin()

if __name__ == "__main__":
    Principal.main()