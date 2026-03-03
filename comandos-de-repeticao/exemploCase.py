import os
os.system('cls')

opc = int(input("\n 1 - Sacar \n 2 - Extrato \n 3 - Sair \n Escolha a opção desejada: "))

# switch case é match case em Python
match opc:
    case 1:
        print("Você escolheu a opção Sacar \n")
        valor = float(input("Digite o valor do saque: "))
        print(f"Sacando da sua conta ... R$ {valor:.2f}")
    case 2:
        print("Você escolheu a opção Extrato \n")
        dias = int(input("Digite a quantidade de dias: "))
        print(f"Retirando extrato de {dias} dias da sua conta ...")
    case 3:
        exit
    case _: # underline = default
        print("Opção inválida!")


# | é o operador OU