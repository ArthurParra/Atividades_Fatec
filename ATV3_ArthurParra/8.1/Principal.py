from login import TelaLogin

# Ponto de entrada do sistema para exibir a tela de login
class Principal:
    @staticmethod
    def main():
        # Abre a janela de login
        TelaLogin()

if __name__ == "__main__":
    Principal.main()