from media_nota import Media

class Principal:
    @staticmethod
    def main():
        #instanciando classe
        media = Media()
        media.iniciar()
        
if __name__ == "__main__":
    Principal.main()