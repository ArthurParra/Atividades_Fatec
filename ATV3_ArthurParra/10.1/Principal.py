from login import TelaLogin

# Ponto de entrada que inicia a tela de login
class Principal:
    @staticmethod
    def main():
        # Inicializa a tela de login (construtor já chama mainloop)
        TelaLogin()

if __name__ == "__main__":
    Principal.main()