import os
os.system('cls')

lista = ["Maria", "João", "Paulo", "Magali"]

busca = input("Digite um nome para procurar: ")

for nome in lista:
    if busca.upper() == nome.upper():
        print(f"{busca} foi encontrado!")
    else:
        print("Não foi encontrado")